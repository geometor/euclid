from __future__ import annotations
import xml.etree.ElementTree as ET
import os
import re
import shutil
from pathlib import Path
from xml.sax.saxutils import escape
import networkx as nx
import json
from PIL import Image, ImageOps


ROMAN_NUMERALS = {
    '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V',
    '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X',
    '11': 'XI', '12': 'XII', '13': 'XIII'
}

SECTION_TYPE_MAP = {
    'Def': 'def',
    'Post': 'post',
    'CN': 'cn',
    'Prop': 'prop'
}

CATEGORIES_KEYWORDS = ['construct', 'describe', 'bisect']
TAGS_KEYWORDS = ['line', 'circle', 'triangle']

def get_taxonomy(enunciation_text: str) -> tuple[list[str], list[str]]:
    categories = []
    tags = []
    
    lower_text = enunciation_text.lower()
    
    for keyword in CATEGORIES_KEYWORDS:
        if keyword in lower_text:
            categories.append(keyword)
            
    for keyword in TAGS_KEYWORDS:
        if keyword in lower_text:
            tags.append(keyword)
            
    return categories, tags

def convert_inline_xml_to_rst(element: ET.Element | None, dependencies: list[str], is_enunciation: bool = False) -> str:
    if element is None:
        return ""

    # Handle non-recursive tags first
    if element.tag == 'ref':
        target_attr = element.get('target')
        if target_attr:
            targets = target_attr.split()
            rst_links = []
            
            for target in targets:
                target_parts = target.split('.')
                canonical_ref = None # Initialize as None
                if len(target_parts) >= 3 and target_parts[0] == 'elem':
                    book_num_str = target_parts[1]
                    book_num_roman = ROMAN_NUMERALS.get(book_num_str)
                    
                    if book_num_roman:
                        if len(target_parts) == 5:
                            # Handle nested definitions like elem.10.def.3.1
                            if target_parts[2] == 'def':
                                group_num = target_parts[3]
                                item_num = target_parts[4]
                                canonical_ref = f"{book_num_roman}.def.{group_num}.{item_num}"
                            elif target_parts[2] == 'c' and target_parts[3] == 'n':
                                section_type_canonical = 'cn'
                                item_num = target_parts[4]
                                canonical_ref = f"{book_num_roman}.{section_type_canonical}.{item_num}"
                            elif target_parts[3] == 'p':
                                prop_num = target_parts[2]
                                porism_num = target_parts[4]
                                canonical_ref = f"{book_num_roman}.{prop_num}.p.{porism_num}"
                            elif target_parts[3] == 'l':
                                prop_num = target_parts[2]
                                lemma_num = target_parts[4]
                                canonical_ref = f"{book_num_roman}.{prop_num}.l.{lemma_num}"
                        elif len(target_parts) == 4 and target_parts[2] == 'post':
                            section_type_canonical = 'post'
                            item_num = target_parts[3]
                            canonical_ref = f"{book_num_roman}.{section_type_canonical}.{item_num}"
                        elif len(target_parts) == 4:
                            section_type_str = target_parts[2]
                            item_num = target_parts[3]
                            section_type_canonical = SECTION_TYPE_MAP.get(section_type_str.capitalize())
                            if section_type_canonical:
                                canonical_ref = f"{book_num_roman}.{section_type_canonical}.{item_num}"
                        elif len(target_parts) == 3:
                            item_num = target_parts[2]
                            if book_num_roman:
                                canonical_ref = f"{book_num_roman}.{item_num}"
                
                if canonical_ref:
                    dependencies.append(canonical_ref)
                else:
                    dependencies.append(target)

                ref_link = canonical_ref if canonical_ref else target
                rst_links.append(f":ref:`{ref_link} <{ref_link}>`")
            
            return " ".join(rst_links)
        else:
            link_text = ''.join(element.itertext()).strip()
            temp_split_parts = re.split(r'[\s.]+', link_text)
            canonical_ref = f"**{link_text}**"
            return f"{canonical_ref}"
    
    if element.tag == 'lb' or element.tag == 'pb':
        return ""
        
    if element.tag == 'figure':
        return "" # Handled by the p-handler which deals with block-level elements

    # Handle container-like tags recursively
    parts = []
    if element.text:
        parts.append(element.text)

    for child in element:
        parts.append(convert_inline_xml_to_rst(child, dependencies, is_enunciation))
        if child.tail:
            parts.append(child.tail)
    
    content = "".join(parts)

    # Apply formatting based on the container's tag
    if element.tag == 'emph':
        if is_enunciation:
            return f"{content.strip()}"
        else:
            return f"``{content.strip()}``"
    elif element.tag == 'term':
        return f"**{content.strip()}**"

    # For other tags (like p, hi, div), just return the processed content
    # Final whitespace cleanup is handled by the caller (flush_inline_parts)
    return content

def parse_book_xml(file_path: str | Path, entry_number_start: int = 0) -> tuple[dict, int]:
    tree = ET.parse(file_path)
    root = tree.getroot()

    book_data = {
        "book_number_roman": None,
        "book_number_arabic": None,
        "sections": []
    }

    div1 = root.find(".//div1[@type='book']")
    if div1 is not None:
        book_data["book_number_arabic"] = div1.attrib.get("n")
        book_data["book_number_roman"] = ROMAN_NUMERALS.get(book_data["book_number_arabic"])
        
        entry_number = entry_number_start # Initialize entry_number here
        for div2 in div1.findall(".//div2"):
            section_type_raw = div2.attrib.get("n")
            # Handle cases like "Def 1", "Prop 1" in Book 10
            type_key = section_type_raw.split()[0] if section_type_raw else ""
            section_type_canonical = SECTION_TYPE_MAP.get(type_key)
            section_head = div2.find("./head")
            section_title = section_head.text if section_head is not None else section_type_raw

            section_data = {
                "type_raw": section_type_raw,
                "type_canonical": section_type_canonical,
                "title": section_title,
                "entries": []
            }

            for div3 in div2.findall(".//div3"):
                entry_number += 1 # Increment entry_number here
                entry_id = div3.attrib.get("id")
                entry_n = div3.attrib.get("n")
                entry_head = div3.find("./head")
                entry_title = entry_head.text if entry_head is not None else entry_id

                # Generate canonical reference for the entry
                canonical_ref = None
                folder_name = None
                # entry_title will be set to canonical_ref later

                if entry_id:
                    parts = entry_id.split('.')
                    book_num_roman = ROMAN_NUMERALS.get(parts[1])

                    if book_num_roman:
                        if len(parts) == 5:
                            # Handle nested definitions like elem.10.def.3.1
                            section_type_str = parts[2]
                            if section_type_str == 'def':
                                group_num = parts[3]
                                item_num = parts[4]
                                canonical_ref = f"{book_num_roman}.def.{group_num}.{item_num}"
                                folder_name = f"def.{group_num}.{item_num}"
                            elif parts[2] == 'c' and parts[3] == 'n':
                                item_num = parts[4]
                                canonical_ref = f"{book_num_roman}.cn.{item_num}"
                                folder_name = f"cn.{item_num}"
                        elif len(parts) == 4 and parts[2] == 'post':
                            item_num = parts[3]
                            canonical_ref = f"{book_num_roman}.post.{item_num}"
                            folder_name = f"post.{item_num}"
                        elif len(parts) == 4:
                            section_type = SECTION_TYPE_MAP.get(parts[2].capitalize())
                            item_num = parts[3]
                            if section_type:
                                canonical_ref = f"{book_num_roman}.{section_type}.{item_num}"
                                folder_name = f"{section_type}.{item_num}"
                        elif len(parts) == 3:
                            item_num = parts[2]
                            canonical_ref = f"{book_num_roman}.{item_num}"
                            folder_name = item_num
                
                entry_title = canonical_ref if canonical_ref else entry_id # Use canonical_ref as title

                entry_content_rst = []
                enunc_text = ""
                dependencies = []
                
                def format_as_blockquote(text):
                    if not text:
                        return ""
                    lines = text.strip().split('\n')
                    indented_lines = [f"   {line}" for line in lines]
                    return "\n".join(indented_lines)

                # Handle Enunciation: either from div4 or the first p tag
                enunc_div = div3.find("./div4[@type='Enunc']")
                if enunc_div is not None:
                    enunc_p = enunc_div.find('p')
                    if enunc_p is not None:
                        enunc_text = convert_inline_xml_to_rst(enunc_p, dependencies, is_enunciation=True)
                        entry_content_rst.append(format_as_blockquote(enunc_text))
                else:
                    # If no Enunc div4, treat the first p as enunciation
                    first_p = div3.find('p')
                    if first_p is not None:
                        enunc_text = convert_inline_xml_to_rst(first_p, dependencies, is_enunciation=True)
                        entry_content_rst.append(format_as_blockquote(enunc_text))
                        # To avoid processing it again, we can remove it or set a flag.
                        # For simplicity, we'll just be careful in the loop below.
                
                # Process remaining elements
                is_first_p = True
                for child in div3:
                    if child.tag == 'head':
                        continue

                    # Skip the enunciation div4 if it exists
                    if child.tag == 'div4' and child.attrib.get('type') == 'Enunc':
                        continue
                    
                    # Skip the first p if it was used as enunciation
                    if child.tag == 'p' and is_first_p and enunc_div is None:
                        is_first_p = False
                        continue
                    is_first_p = False

                    if child.tag == 'div4':
                        div4_type = child.attrib.get('type')
                        if div4_type == 'Proof':
                            pass
                        elif div4_type == 'QED':
                            entry_content_rst.append("\n**Q. E. D.**\n")
                        elif div4_type == 'porism':
                            porism_id = child.attrib.get('id')
                            porism_n = child.attrib.get('n')
                            porism_title = "Porism" # Default
                            if porism_id:
                                parts = porism_id.split('.')
                                if len(parts) == 5:
                                    # elem.3.1.p.1
                                    # We need the prop_num from the parent entry, not from the porism_id itself
                                    # Assuming entry_id is like elem.3.1
                                    parent_parts = entry_id.split('.')
                                    if len(parent_parts) >= 3:
                                        prop_num = parent_parts[2]
                                    else:
                                        prop_num = "UNKNOWN" # Fallback
                                    
                                    p_literal = parts[3] # should be 'p'
                                    porism_num = parts[4]
                                    if p_literal == 'p':
                                        porism_title = f"{book_num_roman}.{prop_num}.p.{porism_num}"
                            
                            porism_content = []
                            for sub_child in child:
                                if sub_child.tag == 'head':
                                    continue
                                elif sub_child.tag == 'p':
                                    inline_rst = convert_inline_xml_to_rst(sub_child, dependencies)
                                    porism_content.append(inline_rst)
                            
                            if porism_id and porism_content:
                                entry_content_rst.append(f"\n.. _{porism_title}:\n")
                                entry_content_rst.append(f"**{porism_title}**\n")
                                entry_content_rst.append("\n".join(porism_content))

                        elif div4_type == 'lemma':
                            lemma_id = child.attrib.get('id')
                            lemma_n = child.attrib.get('n')
                            lemma_title = "Lemma" # Default
                            if lemma_id:
                                parts = lemma_id.split('.')
                                if len(parts) == 5:
                                    # elem.10.9.l.1
                                    # We need the prop_num from the parent entry, not from the lemma_id itself
                                    # Assuming entry_id is like elem.10.9
                                    parent_parts = entry_id.split('.')
                                    if len(parent_parts) >= 3:
                                        prop_num = parent_parts[2]
                                    else:
                                        prop_num = "UNKNOWN" # Fallback

                                    l_literal = parts[3] # should be 'l'
                                    lemma_num = parts[4]
                                    if l_literal == 'l':
                                        lemma_title = f"{book_num_roman}.{prop_num}.l.{lemma_num}"
                            
                            lemma_content = []
                            for sub_child in child:
                                if sub_child.tag == 'head':
                                    continue
                                elif sub_child.tag == 'p':
                                    inline_rst = convert_inline_xml_to_rst(sub_child, dependencies)
                                    lemma_content.append(inline_rst)
                            
                            if lemma_id and lemma_content:
                                entry_content_rst.append(f"\n.. _{lemma_title}:\n")
                                entry_content_rst.append(f"**{lemma_title}**\n")
                                entry_content_rst.append("\n".join(lemma_content))
                            continue

                        
                        # Process content within div4
                        div4_inner_content = []
                        for grand_child in child:
                            if grand_child.tag == 'p':
                                inline_rst = convert_inline_xml_to_rst(grand_child, dependencies)
                                if inline_rst:
                                    div4_inner_content.append(inline_rst)
                            elif grand_child.tag == 'figure':
                                pass
                            elif grand_child.tag == 'hi' and grand_child.attrib.get('rend') == 'center':
                                content = ''.join(grand_child.itertext()).strip()
                                if content:
                                    div4_inner_content.append(f"\n.. container:: center\n\n   {content}\n")
                            else:
                                inline_rst = convert_inline_xml_to_rst(grand_child, dependencies)
                                if inline_rst:
                                    div4_inner_content.append(inline_rst)
                        
                        if div4_inner_content:
                            entry_content_rst.append("\n\n".join(div4_inner_content))

                    elif child.tag == 'p':
                        paragraph_rst_blocks = []
                        current_inline_parts = []

                        def flush_inline_parts():
                            nonlocal current_inline_parts
                            if not current_inline_parts:
                                return
                            full_text = "".join(current_inline_parts)
                            lines = full_text.split('\n')
                            cleaned_lines = [re.sub(r'\s+', ' ', line).strip() for line in lines]
                            final_text = "\n".join(line for line in cleaned_lines if line)
                            if final_text:
                                paragraph_rst_blocks.append(final_text)
                            current_inline_parts = []

                        if child.text:
                            current_inline_parts.append(child.text)

                        for grand_child in child:
                            if grand_child.tag == 'figure':
                                flush_inline_parts()
                            elif grand_child.tag == 'hi' and grand_child.attrib.get('rend') == 'center':
                                flush_inline_parts()
                                content = convert_inline_xml_to_rst(grand_child, dependencies)
                                if content:
                                    indented_content = "\n   ".join(content.splitlines())
                                    paragraph_rst_blocks.append(f"\n.. container:: center\n\n   {indented_content}\n")
                            else:
                                inline_rst = convert_inline_xml_to_rst(grand_child, dependencies)
                                if inline_rst:
                                    current_inline_parts.append(inline_rst)
                            
                            if grand_child.tail:
                                current_inline_parts.append(grand_child.tail)
                        
                        flush_inline_parts()

                        if paragraph_rst_blocks:
                            entry_content_rst.append("\n\n".join(paragraph_rst_blocks))
                    elif child.tag == 'figure':
                        pass
                    elif child.tag == 'hi' and child.attrib.get('rend') == 'center':
                        content = ''.join(child.itertext()).strip()
                        if content:
                            entry_content_rst.append(f"\n.. container:: center\n\n   {content}\n")
                    elif child.tag == 'note':
                        note_title = child.attrib.get('n', '')
                        note_content = []
                        if note_title:
                            note_content.append(f"**{note_title}**")

                        note_dependencies = []  # Discard dependencies found in notes
                        for grand_child in child:
                            if grand_child.tag == 'p':
                                inline_rst = convert_inline_xml_to_rst(grand_child, note_dependencies)
                                if inline_rst:
                                    note_content.append(inline_rst)
                        
                        if note_content:
                            entry_content_rst.append(f"\n.. note::\n")
                            full_note_content = "\n\n".join(note_content)
                            for line in full_note_content.splitlines():
                                entry_content_rst.append(f"   {line}")
                        entry_content_rst.append("") # Add an empty line after the note
                    else:
                        inline_rst = convert_inline_xml_to_rst(child, dependencies)
                        if inline_rst:
                            entry_content_rst.append(inline_rst)



                section_data["entries"].append({
                    "id": entry_id,
                    "n": entry_n,
                    "title": entry_title,
                    "canonical_ref": canonical_ref,
                    "folder_name": folder_name,
                    "content_rst": "\n\n".join(filter(None, entry_content_rst)),
                    "order": entry_n,
                    "number": entry_number,
                    "type": section_type_canonical,
                    "enunciation": enunc_text,
                    "dependencies": dependencies,
                })
            book_data["sections"].append(section_data)
    return book_data, entry_number

def analyze_dependencies(graph: nx.DiGraph, element_ref: str) -> dict[str, list[str]]:
    """
    Analyzes the dependency graph for a given element.
    An edge u -> v means u depends on v.
    """
    analysis = {
        "dependencies": [],  # Things element_ref depends on (descendants)
        "dependents": [] # Things that depend on element_ref (ancestors)
    }
    if element_ref in graph:
        analysis["dependencies"] = sorted(list(nx.descendants(graph, element_ref)))
        analysis["dependents"] = sorted(list(nx.ancestors(graph, element_ref)))
    return analysis

def generate_proof_chain_dot(graph: nx.DiGraph, element_ref: str, ref_to_path_map: dict[str, tuple[str, str]]) -> str:
    if element_ref not in graph:
        return ""

    descendants = nx.descendants(graph, element_ref)
    nodes_in_chain = descendants.union({element_ref})

    dot_lines = [
        "digraph {",
        '  bgcolor="black";',
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];',
        '  edge [color="white", fontcolor="white"];',
        '  rankdir="TB";',
    ]

    # Define nodes with their styles and links
    for node in nodes_in_chain:
        attrs = []
        
        # Determine node type for styling
        node_data_item = graph.nodes[node]
        node_type = node_data_item.get('type', 'unknown')
        
        fillcolor = "#333333" # Default dark gray
        
        # Set color
        if node == element_ref:
            attrs.append('penwidth=3')
            attrs.append('color="white"')
            fillcolor = "#555555"
        else:
            if node_type == 'def':
                fillcolor = "#224422" # Dark Green
            elif node_type == 'prop':
                fillcolor = "#222244" # Dark Blue
            elif node_type == 'cn':
                fillcolor = "#442222" # Dark Red
            elif node_type == 'post':
                fillcolor = "#444422" # Dark Olive
        
        attrs.append(f'fillcolor="{fillcolor}"')

        # Set URL
        path_info = ref_to_path_map.get(node)
        if path_info:
            target_book, target_folder = path_info
            url = f"/heath/{target_book}/{target_folder}/"
            attrs.append(f'URL="{url}"')
            attrs.append('target="_top"')

        attr_str = ", ".join(attrs)
        dot_lines.append(f'  "{node}" [{attr_str}];')

    # Define edges
    for node in nodes_in_chain:
        for pred in graph.predecessors(node):
            if pred in nodes_in_chain:
                dot_lines.append(f'  "{pred}" -> "{node}";')

    dot_lines.append("}")
    return "\n".join(dot_lines)


def generate_rst_files(book_data: dict, output_dir: str | Path, graph: nx.DiGraph, ref_to_path_map: dict[str, tuple[str, str]], metadata: dict) -> None:
    book_roman = book_data["book_number_roman"]
    book_dir = Path(output_dir) / book_roman
    book_dir.mkdir(parents=True, exist_ok=True)

    canonical_images_dir = Path("resources/canonical_images")

    # Create book index.rst
    book_num_arabic = book_data['book_number_arabic']
    book_metadata = metadata.get(book_num_arabic, {})

    title = book_metadata.get('title', f"Book {book_roman}")
    
    book_index_content = [
        f":order: {book_data['book_number_arabic']}",
        ":type: book\n",
        title,
        f"{'=' * len(title)}\n",
    ]

    if book_metadata.get('subtitle') or book_metadata.get('body'):
        if book_metadata.get('subtitle'):
            subtitle = book_metadata['subtitle']
            book_index_content.append(f"   **{subtitle}**\n")
        if book_metadata.get('body'):
            body = book_metadata['body']
            indented_body = "\n   ".join(body.splitlines())
            book_index_content.append(f"   {indented_body}\n")

    # Insert contents directive after the main heading and body
    book_index_content.append("""
.. contents::
   :local:
   :depth: 2

""")

    entry_types_in_book = set()
    
    for section in book_data["sections"]:
        for entry in section["entries"]:
            if entry["folder_name"]:
                entry_dir = book_dir / entry["folder_name"]
                entry_types_in_book.add(entry['type'])
                entry_dir.mkdir(exist_ok=True)

                # Create entry index.rst
                title = entry['canonical_ref']
                underline = "=" * len(title)

                categories, tags = get_taxonomy(entry['enunciation'])

                entry_index_content = [
                    f":order: {entry['order']}",
                    f":number: {entry['number']}",
                    f":type: {entry['type']}",
                ]
                if categories:
                    entry_index_content.append(f":categories: {', '.join(categories)}")
                if tags:
                    entry_index_content.append(f":tags: {', '.join(tags)}")
                
                if entry.get('dependencies'):
                    deps_str = ', '.join(sorted(list(set(entry['dependencies']))))
                    entry_index_content.append(f":dependencies: {deps_str}")

                entry_index_content.append('\n')

                # Copy images and add figure directives
                if canonical_images_dir.exists() and entry['canonical_ref']:
                    image_stem = entry['canonical_ref']
                    
                    image_files = []
                    exact_match = canonical_images_dir / f"{image_stem}.jpg"
                    if exact_match.exists():
                        image_files.append(exact_match)
                    image_files.extend(sorted(canonical_images_dir.glob(f"{image_stem}-*.jpg")))

                    for image_path in image_files:
                        shutil.copy(image_path, entry_dir)
                        entry_index_content.append(f"\n\n.. picture:: {image_path.name}\n")
                
                heath_propositions_dir = Path("resources/heath/propositions")
                if heath_propositions_dir.exists() and entry['canonical_ref']:
                    graphic_stem = entry['canonical_ref']
                    graphic_file = heath_propositions_dir / f"{graphic_stem}.graphic.png"

                    if graphic_file.exists():
                        # Invert and save the graphic image
                        img = Image.open(graphic_file)
                        inverted_img = ImageOps.invert(img.convert('RGB'))
                        inverted_img_path = entry_dir / f"{graphic_file.stem}.inverted.png"
                        inverted_img.save(inverted_img_path)
                        entry_index_content.append(f"\n\n.. picture:: {inverted_img_path.name}\n")
                
                entry_index_content.extend([
                    f".. _{entry['canonical_ref']}:\n",
                    title,
                    underline + "\n",
                    entry['content_rst']
                ])

                if entry.get('analysis'):
                    analysis = entry['analysis']
                    
                    if analysis['dependencies']:
                        entry_index_content.append("\n\nDependency Graph\n----------------\n")
                        dot_content = generate_proof_chain_dot(graph, entry['canonical_ref'], ref_to_path_map)
                        if dot_content:
                            entry_index_content.append(".. graphviz::")
                            entry_index_content.append("")
                            for line in dot_content.splitlines():
                                entry_index_content.append(f"   {line}")
                            entry_index_content.append("")

                    if analysis['dependents']:
                        entry_index_content.append("\n\nRequired for\n------------\n")
                        ref_list = [f":ref:`{req}`" for req in analysis['dependents']]
                        entry_index_content.append(', '.join(ref_list))


                with open(entry_dir / "index.rst", "w") as f:
                    f.write("\n".join(entry_index_content))
                
    # Add collections for each type
    type_titles = {
        'def': 'Definitions',
        'post': 'Postulates',
        'cn': 'Common Notions',
        'prop': 'Propositions'
    }

    # Generate collection sections
    collection_sections = []
    
    sorted_entry_types = sorted(list(entry_types_in_book))
    
    for entry_type in sorted_entry_types:
        if entry_type:
            title = type_titles.get(entry_type, entry_type.capitalize())
            anchor = f"book-{book_roman.lower()}-{entry_type}"
            
            collection_sections.append(f".. _{anchor}:\n")
            collection_sections.append(f"{title}")
            collection_sections.append(f"{'-' * len(title)}\n")
            collection_sections.append(f".. collection::")
            collection_sections.append(f"   :type: {entry_type}")
            collection_sections.append(f"   :sort: number\n")

    # Add the collection sections
    book_index_content.extend(collection_sections)

    with open(book_dir / "index.rst", "w") as f:
        f.write("\n".join(book_index_content))
    print(f"Generated RST files for Book {book_roman}")

def generate_dependency_graph(graph: nx.DiGraph, output_dir: str | Path = "docsrc/elements2") -> None:
    dot_file_path = Path(output_dir) / "dependencies.dot"
    with open(dot_file_path, "w") as f:
        f.write("digraph G {\n")
        f.write('  bgcolor="black";\n')
        f.write('  node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];\n')
        f.write('  edge [color="white", fontcolor="white"];\n')
        f.write('  rankdir="LR";\n')
        f.write('  overlap="false";\n')
        f.write('  splines="true";\n')

        nodes_by_book = {}
        for node in sorted(graph.nodes()):
            parts = node.split('.')
            if len(parts) > 0:
                book_roman = parts[0]
                if book_roman not in nodes_by_book:
                    nodes_by_book[book_roman] = []
                nodes_by_book[book_roman].append(node)

        for book_roman, nodes in sorted(nodes_by_book.items()):
            f.write(f'  subgraph cluster_book_{book_roman} {{\n')
            f.write(f'    label="Book {book_roman}";\n')
            f.write('    color="white";\n')
            f.write('    fontcolor="white";\n')
            for node in nodes:
                # Determine node type for styling
                node_data_item = graph.nodes[node]
                node_type = node_data_item.get('type', 'unknown')
                
                fillcolor = "#333333" # Default dark gray
                if node_type == 'def':
                    fillcolor = "#224422" # Dark Green
                elif node_type == 'prop':
                    fillcolor = "#222244" # Dark Blue
                elif node_type == 'cn':
                    fillcolor = "#442222" # Dark Red
                elif node_type == 'post':
                    fillcolor = "#444422" # Dark Olive
                
                f.write(f'    "{node}" [fillcolor="{fillcolor}"];\n')
            f.write('  }\n')

        for edge in graph.edges():
            f.write(f'  "{edge[0]}" -> "{edge[1]}";\n')
        
        f.write("}\n")
    print(f"Generated dependency graph at {dot_file_path}")

def main():
    print("RST transformation tool")
    output_dir = "docsrc/heath"

    # Clean up existing book directories to prevent orphans
    output_path = Path(output_dir)
    if output_path.exists():
        # Clean all books
        for i in range(1, 14):
            book_roman = ROMAN_NUMERALS.get(str(i))
            if book_roman:
                book_dir = output_path / book_roman
                if book_dir.exists() and book_dir.is_dir():
                    shutil.rmtree(book_dir)
                    print(f"Removed directory: {book_dir}")

    all_books_data = []
    entry_number = 0
    # Process all books
    for i in range(1, 14):
        xml_file_path = f"resources/xml/books/{i:02d}.xml"
        if os.path.exists(xml_file_path):
            print(f"Processing {xml_file_path}")
            book_data, entry_number = parse_book_xml(xml_file_path, entry_number)
            all_books_data.append(book_data)
        else:
            print(f"Warning: XML file not found at {xml_file_path}")

    # Build the dependency graph
    G = nx.DiGraph()
    for book_data in all_books_data:
        for section in book_data["sections"]:
            for entry in section["entries"]:
                if entry["canonical_ref"]:
                    G.add_node(entry["canonical_ref"], **entry)
                    for dep in sorted(list(set(entry["dependencies"]))):
                        G.add_edge(entry["canonical_ref"], dep)

    # Analyze dependencies for each element
    for book_data in all_books_data:
        for section in book_data["sections"]:
            for entry in section["entries"]:
                if entry["canonical_ref"]:
                    analysis = analyze_dependencies(G, entry["canonical_ref"])
                    entry["analysis"] = analysis

    ref_to_path_map = {}
    for book_data in all_books_data:
        book_roman = book_data["book_number_roman"]
        for section in book_data["sections"]:
            for entry in section["entries"]:
                if entry["canonical_ref"] and entry["folder_name"]:
                    ref_to_path_map[entry["canonical_ref"]] = (book_roman, entry["folder_name"])

    # Now generate the RST files with the full dependency info
    metadata = {}
    metadata_path = Path("resources/metadata.json")
    if metadata_path.exists():
        with open(metadata_path, "r") as f:
            metadata = json.load(f)

    for book_data in all_books_data:
        generate_rst_files(book_data, output_dir, G, ref_to_path_map, metadata)

    generate_dependency_graph(G, output_dir)

    # Create the main index.rst for elements2
    main_index_content = [
        ":navigation: header",
        ":order: 2\n",
        "Heath",
        "=====\n",
        ".. collection::",
        "   :type: book",
        "   :title: Books",
        "   :sort: order\n",
    ]
            
    with open(Path(output_dir) / "index.rst", "w") as f:
        f.write("\n".join(main_index_content))
    print("Generated main index.rst for heath")

if __name__ == "__main__":
    main()
