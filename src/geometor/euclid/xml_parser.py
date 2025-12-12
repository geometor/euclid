from __future__ import annotations
import xml.etree.ElementTree as ET
from pathlib import Path

def _convert_element_to_rst(element: ET.Element | None) -> str:
    if element is None:
        return ""

    parts = []
    if element.text:
        parts.append(element.text)

    for child in element:
        if child.tag in ['lb', 'pb']:
            if child.tail:
                parts.append(child.tail)
            continue

        if child.tag == 'emph':
            parts.append(f"``{''.join(child.itertext()).strip()}``")
        elif child.tag == 'ref':
            target = child.get('target')
            link_text = ''.join(child.itertext()).strip()
            parts.append(f":ref:`{link_text} <{target}>`")
        elif child.tag == 'hi':
            parts.append(f"{''.join(child.itertext()).strip()}")
        else:
            parts.append(''.join(child.itertext()).strip())
        
        if child.tail:
            parts.append(child.tail)

    return ''.join(parts).strip().replace('\n', ' ')

def parse_element_xml(file_path: Path):
    """
    Parse a single element XML file.

    Args:
        file_path (Path): The path to the XML file.

    Returns:
        dict: A dictionary containing the parsed element data (id, type, head, enunciation, etc.).
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    element_id = root.get('id')
    element_type = root.get('type')
    element_number = root.get('n')
    
    head = root.find('head').text if root.find('head') is not None else ''
    
    enunciation_p = root.find(".//div4[@type='Enunc']/p")
    enunciation = _convert_element_to_rst(enunciation_p)

    proof_div = root.find(".//div4[@type='Proof']")
    proof_paragraphs = []
    if proof_div is not None:
        for p in proof_div.findall('p'):
            proof_paragraphs.append(_convert_element_to_rst(p))
    
    proof = "\n\n".join(proof_paragraphs)

    # Fallback for elements without explicit Enunc/Proof sections
    if not enunciation and not proof:
        all_paragraphs = root.findall('p')
        if all_paragraphs:
            enunciation = _convert_element_to_rst(all_paragraphs[0])
            if len(all_paragraphs) > 1:
                proof_paragraphs = [_convert_element_to_rst(p) for p in all_paragraphs[1:]]
                proof = "\n\n".join(proof_paragraphs)

    qed_p = root.find(".//div4[@type='QED']/p")
    qed = _convert_element_to_rst(qed_p)

    porism_div = root.find(".//div4[@type='porism']")
    porism = None
    if porism_div is not None:
        porism_head = porism_div.find('head').text if porism_div.find('head') is not None else ''
        porism_paragraphs = []
        for p in porism_div.findall('p'):
            porism_paragraphs.append(_convert_element_to_rst(p))
        porism = {
            'head': porism_head,
            'text': "\n\n".join(porism_paragraphs)
        }

    dependencies = [ref.get('target') for ref in root.findall('.//ref')]

    return {
        'id': element_id,
        'type': element_type,
        'number': element_number,
        'head': head,
        'enunciation': enunciation,
        'proof': proof,
        'qed': qed,
        'porism': porism,
        'dependencies': dependencies,
    }
