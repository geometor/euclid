"""Tests for Euclid's *Data* (*Δεδομένα*) 4-track Book Codex, concordance, SVGs, and Sphinx track."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from geometor.euclid.data_codex import (
    build_data_dependency_dag,
    load_data_apparatus,
    load_data_concordance,
    propositions_by_unit,
    propositions_citing_elements,
    validate_data_concordance,
)
from geometor.euclid.sphinx_ext import (
    GREEK_TRACK_LABEL,
    configure_local_intersphinx,
    register_greek_book_track,
    setup,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_RESOURCES = REPO_ROOT / "resources" / "data"
HEATH_RESOURCES = REPO_ROOT / "resources" / "heath"
DATA_DOCSRC = REPO_ROOT / "docsrc" / "data"
FIGURES_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"


@dataclass
class _DummyEnv:
    """Minimal Sphinx build environment stub for testing ``detect_companion_tracks``."""

    found_docs: set[str]


def test_zero_python_files_in_data_trees() -> None:
    """Ensure zero embedded Python scripts exist in resources/data or docsrc/data."""
    res_py = sorted(DATA_RESOURCES.rglob("*.py"))
    doc_py = sorted(DATA_DOCSRC.rglob("*.py"))
    assert res_py == [], f"Unexpected .py files in resources/data: {res_py}"
    assert doc_py == [], f"Unexpected .py files in docsrc/data: {doc_py}"


def test_data_concordance_schema_and_dag() -> None:
    """Verify the 7 units, 15 definitions, 94 propositions, and causal dependency DAG."""
    conc = load_data_concordance()
    assert validate_data_concordance(conc) == []
    assert len(conc.units) == 7
    assert len(conc.definitions) == 15
    assert len(conc.propositions) == 94

    authentic_flags = [d.authentic for d in conc.definitions]
    assert authentic_flags[:12] == [True] * 12
    assert authentic_flags[12:] == [False] * 3

    expected_unit_counts = {1: 24, 2: 14, 3: 17, 4: 12, 5: 16, 6: 11}
    for unit_idx, expected_len in expected_unit_counts.items():
        unit_props = propositions_by_unit(conc, unit_idx)
        assert len(unit_props) == expected_len

    vi28_props = propositions_citing_elements(conc, "VI.28")
    assert any(p.id == "D.58" for p in vi28_props)

    dag = build_data_dependency_dag(conc)
    assert len(dag) == 109
    assert "D.59" in dag["D.84"]
    assert "D.58" in dag["D.85"]


def test_data_apparatus_registries_and_elements_targets() -> None:
    """Verify apparatus registries and ensure all cited Elements propositions resolve."""
    conc = load_data_concordance()
    apparatus = load_data_apparatus()
    assert len(apparatus["enunciations"]) == 109
    assert len(apparatus["citations"]) >= 18
    assert len(apparatus["persons"]) >= 20
    assert len(apparatus["glossary"]) >= 24

    heath_enunciations = json.loads(
        (HEATH_RESOURCES / "enunciations.json").read_text(encoding="utf-8")
    )
    heath_keys = {k.lower() for k in heath_enunciations}
    missing = [
        (p.id, dep)
        for p in conc.propositions
        for dep in p.elements_deps
        if dep.lower() not in heath_keys
    ]
    assert missing == [], f"Unresolved Heath Elements dependencies: {missing}"


def test_data_codex_four_track_rst_files_and_anchors() -> None:
    """Ensure all 448 canonical atomic RST files and all 218 bilingual RST anchors exist in docsrc/data."""
    conc = load_data_concordance()
    rst_files = sorted(DATA_DOCSRC.rglob("*.rst"))
    assert len(rst_files) == 470

    for root_file in (
        "index.rst",
        "title-el.rst",
        "concordance.rst",
        "bibliography.rst",
        "people/index.rst",
        "glossary.rst",
        "protheoria/index.rst",
        "protheoria/greek.rst",
        "protheoria/summary.rst",
        "protheoria/notes.rst",
        "definitions/index.rst",
        "propositions/index.rst",
    ):
        assert (DATA_DOCSRC / root_file).is_file(), f"Missing {root_file}"

    for d in conc.definitions:
        d_dir = DATA_DOCSRC / "definitions" / f"{d.number:02d}"
        for track in ("index", "greek", "summary", "notes"):
            track_path = d_dir / f"{track}.rst"
            assert track_path.is_file(), f"Missing definition track {track_path}"
        assert f".. _{d.id}:" in (d_dir / "index.rst").read_text(encoding="utf-8")
        assert f".. _{d.id}.el:" in (d_dir / "greek.rst").read_text(encoding="utf-8")

    for p in conc.propositions:
        p_dir = DATA_DOCSRC / "propositions" / f"{p.number:02d}"
        for track in ("index", "greek", "summary", "notes"):
            track_path = p_dir / f"{track}.rst"
            assert track_path.is_file(), f"Missing proposition track {track_path}"
        assert f".. _{p.id}:" in (p_dir / "index.rst").read_text(encoding="utf-8")
        assert f".. _{p.id}.el:" in (p_dir / "greek.rst").read_text(encoding="utf-8")


def test_data_svgs_well_formed_and_geom_refs_resolve() -> None:
    """Verify all 8 Data SVGs parse cleanly and match every :g: reference in docsrc/data."""
    svg_refs_by_gid: dict[str, set[str]] = {}
    svg_paths = sorted(FIGURES_DIR.glob("data_0*.svg"))
    assert len(svg_paths) == 8

    for svg_path in svg_paths:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert root.attrib.get("viewBox", "").strip()
        gid = root.attrib.get("data-graphic-id", "").strip()
        assert gid, f"Missing data-graphic-id on {svg_path}"
        refs = {
            elem.attrib["data-ref"]
            for elem in root.iter()
            if "data-ref" in elem.attrib
        }
        assert len(refs) >= 8, f"Expected interactive data-ref primitives in {svg_path}"
        svg_refs_by_gid[gid] = refs

    unresolved_g: list[tuple[str, str, str]] = []
    for rst_path in sorted(DATA_DOCSRC.rglob("*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        for match in re.finditer(r":g:`[^`]*<([^:`]+):([^>`]+)>`", text):
            gid, ref_tok = match.group(1).strip(), match.group(2).strip()
            if gid not in svg_refs_by_gid or ref_tok not in svg_refs_by_gid[gid]:
                unresolved_g.append((rst_path.name, gid, ref_tok))
    assert unresolved_g == [], f"Unresolved :g: tokens in docsrc/data: {unresolved_g}"


def test_sphinx_greek_track_registration_preserves_heath_tracks(tmp_path: Path) -> None:
    """Verify Greek track registration gives 4 tracks on Data and leaves 2-track Heath intact."""
    import importlib.util
    import sys

    publish_src = REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"
    if importlib.util.find_spec("photon_platform") is None and publish_src.is_dir():
        sys.path.insert(0, str(publish_src))

    meta = setup(object())
    assert meta["parallel_read_safe"] is True
    register_greek_book_track()

    if importlib.util.find_spec("photon_platform") is not None:
        from photon_platform.publish import book

        env = _DummyEnv(
            found_docs={
                "data/propositions/01/index",
                "data/propositions/01/greek",
                "data/propositions/01/summary",
                "data/propositions/01/notes",
                "heath/volume_I/book_i/propositions/0001-en",
                "heath/volume_I/book_i/propositions/0001-notes",
            }
        )

        data_tracks = book.detect_companion_tracks(
            env, "data/propositions/01/greek"
        )
        assert [t["key"] for t in data_tracks] == ["en", "el", "summary", "notes"]
        el_track = next(t for t in data_tracks if t["key"] == "el")
        assert el_track["label"] == GREEK_TRACK_LABEL
        assert el_track["active"] is True

        idx_tracks = book.detect_companion_tracks(
            env, "data/propositions/01/index"
        )
        assert [t["key"] for t in idx_tracks] == ["en", "el", "summary", "notes"]
        en_track = next(t for t in idx_tracks if t["key"] == "en")
        assert en_track["active"] is True

        heath_tracks = book.detect_companion_tracks(
            env, "heath/volume_I/book_i/propositions/0001-en"
        )
        assert [t["key"] for t in heath_tracks] == ["en", "notes"]

    # Verify offline-safe local intersphinx helper drops None remote targets
    fake_proj = tmp_path / "euclid"
    fake_proj.mkdir()
    sister_inv = tmp_path / "elements" / "docs"
    sister_inv.mkdir(parents=True)
    (sister_inv / "objects.inv").write_bytes(b"# Sphinx inventory version 2\n")

    mapping: dict[str, tuple[str, str | None]] = {
        "remote_only": ("https://example.org", None),
    }
    configure_local_intersphinx(mapping, fake_proj)
    assert "remote_only" not in mapping
    assert "elements" in mapping
