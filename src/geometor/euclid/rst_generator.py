from __future__ import annotations
from geometor.elements.xml_parser import parse_element_xml
from pathlib import Path

def generate_rst_from_xml(xml_file_path: Path, output_dir: Path):
    """
    Generate an RST file from an XML element file.

    Args:
        xml_file_path (Path): The path to the input XML file.
        output_dir (Path): The directory where the output RST file will be saved.
    """
    parsed_data = parse_element_xml(xml_file_path)

    element_id = parsed_data['id']
    element_type = parsed_data['type']
    element_number = parsed_data['number']
    head = parsed_data['head']
    enunciation = parsed_data['enunciation']
    proof = parsed_data.get('proof', '')
    qed = parsed_data.get('qed', '')
    porism = parsed_data.get('porism')
    dependencies = parsed_data.get('dependencies', [])

    # Create a semantic filename (e.g., book1-proposition1.rst)
    # This needs more sophisticated logic for actual semantic naming
    # For now, a simple conversion from elem.1.1.xml to book1/prop1.rst
    book_num = int(element_id.split('.')[1])
    type_abbr = {'proposition': 'prop', 'definition': 'def', 'postulate': 'post', 'common_notion': 'cn'}
    element_type_short = type_abbr.get(element_type, element_type)
    
    # Create book subdirectory if it doesn't exist
    book_output_dir = output_dir / f"book{book_num:02}"
    book_output_dir.mkdir(parents=True, exist_ok=True)

    rst_filename = f"{element_id}.rst"
    rst_file_path = book_output_dir / rst_filename

    rst_content = f""":category: {element_type}

.. _{element_id}:

{head}
{'=' * len(head)}

    {enunciation}

"""

    if proof:
        rst_content += f"""

{proof}
"""

    if qed:
        rst_content += f"""

**Q.E.D.** {qed}
"""

    if porism:
        rst_content += f"""
.. _{element_id}.p.1:

{porism['head']}
{'-' * len(porism['head'])}

{porism['text']}
"""

    if dependencies:
        rst_content += """

Dependencies
------------
"""
        for dep in dependencies:
            rst_content += f"- :ref:`{dep}`\n"


    rst_file_path.write_text(rst_content)
    print(f"Generated RST file: {rst_file_path}")
