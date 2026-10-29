"""Build dependency graphs and inject Graphviz proof chains into composed RST files under docsrc/heath/."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import networkx as nx

ROMAN_NUMERALS = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
    "11": "XI",
    "12": "XII",
    "13": "XIII",
}

ROMAN_TO_INT = {v: int(k) for k, v in ROMAN_NUMERALS.items()}

VALID_BOOKS = set(ROMAN_NUMERALS.values())

SECTION_TYPE_ORDER = {
    "def": 1,
    "post": 2,
    "cn": 3,
    "prop": 4,
}

_JUST_ROLE_RE = re.compile(r":just:`([^`]+)`")
_DIR_JUST_RE = re.compile(
    r"^\.\.\s+(?:assertion|subclause|sub-clause)::[ \t]+([^\n]+)",
    re.MULTILINE,
)
_EXPLICIT_LABEL_RE = re.compile(r"^\.\.\s+_([^:\n]+):\s*$", re.MULTILINE)


def infer_justification_target(
    display: str, current_book: Optional[str] = None
) -> Optional[str]:
    """Infer canonical target ID(s) from justification text when <target> is omitted."""
    s = (display or "").strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    if not s or re.match(
        r"^(?:Q\.\s*\$?E\$?\.|[*]?id[*]?\.|above|from above|Part\s+\d|First part|Prop\.\s*D|Simson|Pappus|\(\d+\))",
        s,
        re.IGNORECASE,
    ):
        return None

    m_deff = re.search(
        r"\b([IVXLCDM]+)\.\s*Deff?\.\s*(III|II)(?:\.\s*(\d+))?",
        s,
        re.IGNORECASE,
    )
    if m_deff and m_deff.group(1).upper() in VALID_BOOKS:
        bk = m_deff.group(1).upper()
        sub = m_deff.group(2).lower()
        num = m_deff.group(3)
        return f"{bk}.def.{sub}.{num}" if num else f"{bk}.def.{sub}"

    bk_default = (current_book or "I").upper()
    m_post = re.match(r"^Post\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_post:
        return f"I.post.{m_post.group(1)}"
    m_cn = re.match(r"^C\.\s*N\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_cn:
        return f"I.cn.{m_cn.group(1)}"
    m_def_bare = re.match(r"^Def\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_def_bare:
        return f"{bk_default}.def.{m_def_bare.group(1)}"

    results: List[str] = []
    pat = re.compile(
        r"\b([IVXLCDM]+)\.\s*(?:(Def\.?)\s*(\d+)|(\d+)(?:\s*(?:,|and|or)\s*(\d+))?)",
        re.IGNORECASE,
    )
    for m in pat.finditer(s):
        bk = m.group(1).upper()
        if bk not in VALID_BOOKS:
            continue
        if m.group(2):
            results.append(f"{bk}.def.{m.group(3)}")
        else:
            results.append(f"{bk}.{m.group(4)}")
            if m.group(5):
                results.append(f"{bk}.{m.group(5)}")
    if results:
        return ", ".join(dict.fromkeys(results))
    return None


def parse_justification_arg(
    raw_arg: str, current_book: Optional[str] = None
) -> Tuple[str, Optional[str]]:
    """Parse a justification string into (display_text, target_id)."""
    text = (raw_arg or "").strip()
    if not text:
        return "", None

    match = re.match(r"^(.*?)\s*<([^>]+)>$", text)
    if match:
        display = match.group(1).strip()
        target = match.group(2).strip()
        if not display:
            display = f"[{target}]"
        return display, target

    if text.startswith("[") and text.endswith("]"):
        return text, infer_justification_target(text, current_book=current_book)

    if re.match(r"^[A-Za-z0-9_.-]+$", text) and "." in text:
        return f"[{text}]", text

    return text, infer_justification_target(text, current_book=current_book)


def canonical_sort_key(ref_id: str) -> Tuple[int, int, int, int, str]:
    """Return a deterministic sort key for canonical Euclid IDs (e.g. I.def.15, I.post.1, I.cn.4, I.47)."""
    parts = ref_id.split(".")
    if not parts:
        return (999, 999, 0, 0, ref_id)

    book_num = ROMAN_TO_INT.get(parts[0].upper(), 999)
    if len(parts) == 2 and parts[1].isdigit():
        return (book_num, SECTION_TYPE_ORDER["prop"], 0, int(parts[1]), ref_id)

    sec_type = parts[1].lower() if len(parts) > 1 else ""
    type_order = SECTION_TYPE_ORDER.get(sec_type, 99)

    group_order = 0
    item_num = 0
    if len(parts) == 3 and parts[2].isdigit():
        item_num = int(parts[2])
    elif len(parts) == 4:
        sub_map = {"i": 1, "ii": 2, "iii": 3}
        group_order = sub_map.get(parts[2].lower(), 0)
        if parts[3].isdigit():
            item_num = int(parts[3])

    return (book_num, type_order, group_order, item_num, ref_id)


def get_node_type(ref_id: str) -> str:
    """Classify a canonical Euclid ID into 'prop', 'def', 'post', or 'cn'."""
    parts = ref_id.split(".")
    if len(parts) >= 2:
        sec = parts[1].lower()
        if sec in ("def", "post", "cn"):
            return sec
        if sec.isdigit():
            return "prop"
    return "unknown"


def _docutils_anchor_id(label: str) -> str:
    """Convert an RST explicit label like 'I.def.15' into its docutils HTML id 'i-def-15'."""
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def extract_dependencies_from_rst_body(
    rst_body: str, current_book: Optional[str] = None
) -> List[str]:
    """Extract sorted unique canonical dependency IDs from a composed RST body.

    Strips footnote definitions and trailing commentary dividers so only dependencies
    from Euclid's proof and porisms are recorded.
    """
    # Strip trailing commentary link / hidden toctree / dependency sections
    proof_part = re.split(r"\n----\n|\nDependency Graph\n----------------", rst_body, maxsplit=1)[0]
    # Strip footnote definition lines (.. [#f...])
    cleaned_lines: List[str] = []
    in_footnote = False
    for line in proof_part.splitlines():
        if re.match(r"^\.\.\s+\[#[^\]]+\]", line):
            in_footnote = True
            continue
        if in_footnote:
            if not line.strip() or line.startswith("   ") or line.startswith("\t"):
                continue
            in_footnote = False
        cleaned_lines.append(line)
    cleaned_body = "\n".join(cleaned_lines)

    deps: Set[str] = set()
    for m in _JUST_ROLE_RE.finditer(cleaned_body):
        _, target = parse_justification_arg(m.group(1), current_book=current_book)
        if target:
            for part in target.split(","):
                p = part.strip()
                if p:
                    deps.add(p)

    for m in _DIR_JUST_RE.finditer(cleaned_body):
        _, target = parse_justification_arg(m.group(1), current_book=current_book)
        if target:
            for part in target.split(","):
                p = part.strip()
                if p:
                    deps.add(p)

    return sorted(deps, key=canonical_sort_key)


def _strip_existing_graph_sections(rst_text: str) -> str:
    """Remove any previously injected Dependency Graph and Required for sections from rst_text."""
    pattern = re.compile(
        r"\n*Dependency Graph\n----------------\n.*?(?=\n----\n|\n\.\.\s+toctree::|\Z)",
        re.DOTALL,
    )
    cleaned = pattern.sub("", rst_text)
    req_pattern = re.compile(
        r"\n*Required for\n------------\n.*?(?=\n----\n|\n\.\.\s+toctree::|\Z)",
        re.DOTALL,
    )
    cleaned = req_pattern.sub("", cleaned)
    return cleaned


def _update_frontmatter_dependencies(rst_text: str, deps: List[str]) -> str:
    """Insert or update the :dependencies: field in the top metadata block of rst_text."""
    lines = rst_text.splitlines()
    dep_line = f":dependencies: {', '.join(deps)}" if deps else None

    end_meta_idx = 0
    existing_dep_idx: Optional[int] = None
    for idx, line in enumerate(lines):
        s = line.strip()
        if s.startswith(":") and ":" in s[1:]:
            end_meta_idx = idx + 1
            if s.startswith(":dependencies:"):
                existing_dep_idx = idx
        elif not s and end_meta_idx > 0:
            break
        else:
            break

    if existing_dep_idx is not None:
        if dep_line:
            lines[existing_dep_idx] = dep_line
        else:
            lines.pop(existing_dep_idx)
    elif dep_line and end_meta_idx > 0:
        lines.insert(end_meta_idx, dep_line)

    return "\n".join(lines) + "\n"


def clean_rst_enunciation(raw_text: str) -> str:
    """Strip RST inline roles, footnote markers, emphasis, and item numbers from an enunciation or definition."""
    s = re.sub(r"\\?\s*\[#[^\]]+\]_", "", raw_text or "")
    s = re.sub(r"\s*:just:`[^`]+`", "", s)
    s = re.sub(r":[a-z]+:`([^`<]+?)\s*<[^>]+>`", r"\1", s)
    s = re.sub(r":[a-z]+:`([^`]+)`", r"\1", s)
    s = s.replace("**", "").replace("*", "").replace("$", "")
    s = re.sub(r"^(?:\[\d+\]\s*)?\d+\.\s*", "", s.strip())
    s = re.sub(r"\s+", " ", s).strip()
    if s.endswith(";"):
        s = s[:-1].rstrip() + "."
    return s


def truncate_enunciation(text: str, max_chars: int = 180) -> str:
    """Collapse whitespace and truncate a long enunciation cleanly at a word boundary."""
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    if len(cleaned) <= max_chars:
        return cleaned
    cut = cleaned[:max_chars].rsplit(" ", 1)[0].rstrip(".,;:")
    return f"{cut}…"


def format_node_tooltip(
    node_id: str, enunciations: Dict[str, str], max_chars: int = 180
) -> str:
    """Format a truncated enunciation tooltip for a Graphviz node."""
    enun = enunciations.get(node_id)
    if not enun and node_id.lower().startswith("viii.def."):
        enun = enunciations.get("VII." + node_id[5:])
    if not enun:
        for k, v in enunciations.items():
            if k.lower() == node_id.lower():
                enun = v
                break
    if not enun:
        return node_id
    short_text = truncate_enunciation(enun, max_chars=max_chars)
    return f"{node_id}: {short_text}"


def generate_proof_chain_dot(
    graph: nx.DiGraph,
    element_ref: str,
    current_dir: Path,
    label_to_target: Dict[str, Tuple[Path, Optional[str]]],
    enunciations: Optional[Dict[str, str]] = None,
) -> str:
    """Generate a Graphviz DOT string for the transitive proof chain of element_ref.

    Note: Sphinx's ``sphinx.ext.graphviz.fix_svg_relative_paths`` resolves ``URL``
    attributes in DOT relative to the source RST document's directory (``current_dir``)
    and rewrites them to be relative to ``_images/`` in the output SVG.
    """
    import os

    if element_ref not in graph:
        return ""

    descendants = nx.descendants(graph, element_ref)
    if not descendants:
        return ""

    nodes_in_chain = sorted(descendants.union({element_ref}), key=canonical_sort_key)

    dot_lines = [
        "digraph {",
        '  bgcolor="transparent";',
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];',
        '  edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];',
        '  rankdir="TB";',
    ]

    for node in nodes_in_chain:
        attrs = [f'label="{node}"']
        node_type = get_node_type(node)

        fillcolor = "#333333"
        if node == element_ref:
            attrs.append("penwidth=2.5")
            attrs.append('color="#e8b85a"')
            fillcolor = "#4a453b"
        else:
            if node_type == "def":
                fillcolor = "#224422"
            elif node_type == "prop":
                fillcolor = "#222244"
            elif node_type == "cn":
                fillcolor = "#442222"
            elif node_type == "post":
                fillcolor = "#444422"

        attrs.append(f'fillcolor="{fillcolor}"')

        tooltip_str = format_node_tooltip(node, enunciations or {})
        esc_tooltip = tooltip_str.replace("\\", "\\\\").replace('"', '\\"')
        attrs.append(f'tooltip="{esc_tooltip}"')

        target_info = label_to_target.get(node.lower())
        if not target_info and node.lower().startswith("viii.def."):
            target_info = label_to_target.get("vii." + node.lower()[5:])
        if target_info:
            target_html_path, anchor = target_info
            rel_path = os.path.relpath(target_html_path, start=current_dir).replace("\\", "/")
            url = f"{rel_path}#{anchor}" if anchor else rel_path
            attrs.append(f'URL="{url}"')
            attrs.append('target="_top"')

        attr_str = ", ".join(attrs)
        dot_lines.append(f'  "{node}" [{attr_str}];')

    for node in nodes_in_chain:
        for pred in sorted(graph.predecessors(node), key=canonical_sort_key):
            if pred in nodes_in_chain:
                dot_lines.append(f'  "{pred}" -> "{node}";')

    dot_lines.append("}")
    return "\n".join(dot_lines)


def build_graph(
    heath_out_dir: Path | None = None,
    inject_rst: bool = True,
) -> Tuple[nx.DiGraph, Dict[str, Any]]:
    """Build the NetworkX dependency graph from the composed RST files under docsrc/heath/.

    If inject_rst is True, updates :dependencies:, writes resources/heath/enunciations.json,
    and injects the 'Dependency Graph' (.. graphviz::) and 'Required for' sections into
    every proposition's index.rst.
    """
    if heath_out_dir is None:
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent.parent
        heath_out_dir = project_root / "docsrc" / "heath"

    heath_out_dir = Path(heath_out_dir)

    # 1. Index all explicit labels and enunciations across docsrc/heath/
    label_to_target: Dict[str, Tuple[Path, Optional[str]]] = {}
    enunciations: Dict[str, str] = {}
    prop_files: List[Tuple[str, str, Path]] = []

    for rst_path in sorted(heath_out_dir.rglob("index.rst")):
        html_path = rst_path.with_suffix(".html")
        txt = rst_path.read_text(encoding="utf-8")

        m_cid = re.search(r"^:canonical_id:\s*(.+)$", txt, re.MULTILINE)
        m_type = re.search(r"^:type:\s*(.+)$", txt, re.MULTILINE)
        m_book = re.search(r"^:book:\s*(.+)$", txt, re.MULTILINE)
        m_title = re.search(r"^:title:\s*(.+)$", txt, re.MULTILINE)

        cid = m_cid.group(1).strip() if m_cid else ""
        utype = m_type.group(1).strip() if m_type else ""
        book_roman = m_book.group(1).strip() if m_book else "I"
        title_str = m_title.group(1).strip() if m_title else ""

        if cid:
            label_to_target[cid.lower()] = (html_path, None)

        for m_lbl in _EXPLICIT_LABEL_RE.finditer(txt):
            lbl = m_lbl.group(1).strip()
            if lbl.lower() == cid.lower():
                label_to_target[lbl.lower()] = (html_path, None)
            else:
                anchor = _docutils_anchor_id(lbl)
                label_to_target[lbl.lower()] = (html_path, anchor)

        if utype == "proposition" and cid:
            prop_files.append((cid, book_roman, rst_path))
            m_enun = re.search(
                r"\.\.\s+enunciation::\s*\n+((?:[ \t]+.+\n?|\n)+)", txt
            )
            if m_enun:
                cleaned_enun = clean_rst_enunciation(m_enun.group(1))
                if cleaned_enun:
                    enunciations[cid] = cleaned_enun
        elif utype in ("definitions", "postulates", "common_notions"):
            if cid and title_str:
                enunciations[cid] = title_str
            for m_item in re.finditer(
                r"^\.\.\s+_([^:\n]+):\s*\n+((?:(?!\.\.\s+_).+\n?)+)",
                txt,
                re.MULTILINE,
            ):
                lbl = m_item.group(1).strip()
                if lbl.lower().startswith("folio-") or lbl.lower() == cid.lower():
                    continue
                para = m_item.group(2).strip().split("\n\n")[0]
                cleaned_item = clean_rst_enunciation(para)
                if cleaned_item:
                    enunciations[lbl] = cleaned_item

    for k, v in list(enunciations.items()):
        if k.startswith("VII.def."):
            enunciations["VIII." + k[4:]] = v

    # Save sorted enunciations registry to resources/heath/enunciations.json
    sorted_enunciations = dict(
        sorted(enunciations.items(), key=lambda kv: canonical_sort_key(kv[0]))
    )
    enun_json_path = heath_out_dir.parent.parent / "resources" / "heath" / "enunciations.json"
    if enun_json_path.parent.is_dir():
        enun_json_path.write_text(
            json.dumps(sorted_enunciations, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    # 2. Extract dependencies from each composed proposition index.rst and build DiGraph
    G = nx.DiGraph()
    prop_deps_map: Dict[str, List[str]] = {}

    for cid, book_roman, rst_path in prop_files:
        raw_txt = rst_path.read_text(encoding="utf-8")
        cleaned_txt = _strip_existing_graph_sections(raw_txt)
        deps = [
            d
            for d in extract_dependencies_from_rst_body(cleaned_txt, current_book=book_roman)
            if d != cid
        ]
        prop_deps_map[cid] = deps

        G.add_node(
            cid,
            canonical_ref=cid,
            type="prop",
            book=book_roman,
            dependencies=deps,
            path=str(rst_path),
        )
        for dep in deps:
            if dep not in G:
                G.add_node(
                    dep,
                    canonical_ref=dep,
                    type=get_node_type(dep),
                    book=dep.split(".")[0] if "." in dep else book_roman,
                    dependencies=[],
                )
            G.add_edge(cid, dep)

    # 3. Inject Dependency Graph and Required for sections into composed proposition files
    graphs_injected = 0
    required_for_injected = 0

    if inject_rst:
        for cid, book_roman, rst_path in prop_files:
            raw_txt = rst_path.read_text(encoding="utf-8")
            cleaned_txt = _strip_existing_graph_sections(raw_txt)
            deps = prop_deps_map.get(cid, [])
            updated_txt = _update_frontmatter_dependencies(cleaned_txt, deps)

            extra_sections: List[str] = []

            dot_str = generate_proof_chain_dot(
                G, cid, rst_path.parent, label_to_target, enunciations=sorted_enunciations
            )
            if dot_str:
                indented_dot = "\n".join(f"   {line}" for line in dot_str.splitlines())
                extra_sections.append(
                    f"Dependency Graph\n----------------\n\n.. graphviz::\n\n{indented_dot}"
                )
                graphs_injected += 1

            ancestors = sorted(
                [a for a in nx.ancestors(G, cid) if get_node_type(a) == "prop"],
                key=canonical_sort_key,
            )
            if ancestors:
                ref_links = [f":ref:`{req} <{req}>`" for req in ancestors]
                extra_sections.append(
                    f"Required for\n------------\n\n{', '.join(ref_links)}"
                )
                required_for_injected += 1

            if extra_sections:
                insertion = "\n\n" + "\n\n".join(extra_sections) + "\n\n"
                # Insert before trailing commentary divider (`----`) or hidden `.. toctree::`
                m_tail = re.search(
                    r"\n(----\n\nSee :ref:`Commentary|\.\.\s+toctree::\n\s+:hidden:)",
                    updated_txt,
                )
                if m_tail:
                    split_pos = m_tail.start()
                    updated_txt = (
                        updated_txt[:split_pos].rstrip()
                        + insertion
                        + updated_txt[split_pos:].lstrip("\n")
                    )
                else:
                    updated_txt = updated_txt.rstrip() + insertion

            if updated_txt != raw_txt:
                rst_path.write_text(updated_txt.rstrip() + "\n", encoding="utf-8")

    stats = {
        "propositions_scanned": len(prop_files),
        "enunciations_indexed": len(sorted_enunciations),
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "graphs_injected": graphs_injected,
        "required_for_injected": required_for_injected,
    }
    return G, stats


if __name__ == "__main__":
    _, summary = build_graph()
    print(summary)
