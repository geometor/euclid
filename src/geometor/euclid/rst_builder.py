from pathlib import Path
from .rst_generator import generate_rst_from_xml

def build_rst_docs(xml_dir: Path, output_dir: Path):
    """
    Parses all XML files in xml_dir and generates RST files in output_dir.
    """
    for xml_file in xml_dir.glob("*.xml"):
        generate_rst_from_xml(xml_file, output_dir)
