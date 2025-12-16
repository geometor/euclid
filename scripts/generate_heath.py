
from pathlib import Path
import json
import networkx as nx
from geometor.euclid.transform import parse_book_xml, generate_heath_rst

def load_book_descriptions(path: Path) -> dict:
    with open(path, 'r') as f:
        data = json.load(f)
    
    # Transform list to dict keyed by book number
    descriptions = {}
    for item in data:
        # folder name is like "01.book-1", "02.book-2"
        # we can extract the integer from the folder name or just assume order
        folder = item['folder']
        # extract "1" from "01.book-1"
        try:
            book_num = str(int(folder.split('.')[0]))
            descriptions[book_num] = item
        except:
            print(f"Could not parse book number from {folder}")
            
    return descriptions

def main():
    root_dir = Path(__file__).parent.parent
    xml_dir = root_dir / "resources/xml/books"
    output_dir = root_dir / "docsrc/heath"
    desc_path = root_dir / "resources/book_descriptions.json"
    
    print(f"Loading descriptions from {desc_path}")
    descriptions = load_book_descriptions(desc_path)
    
    # Initialize dependency graph (empty for now or load if existing logic permits)
    graph = nx.DiGraph()
    ref_to_path_map = {}

    # Get XML files
    xml_files = sorted(list(xml_dir.glob("*.xml")))
    
    for xml_file in xml_files:
        print(f"Processing {xml_file.name}...")
        try:
            book_data, _ = parse_book_xml(xml_file)
            
            book_num = book_data['book_number_arabic']
            print(f"  Book {book_num}")
            
            # Merge description data into metadata
            metadata = {}
            if book_num in descriptions:
                desc = descriptions[book_num]
                metadata[book_num] = {
                    "title": f"Book {book_data['book_number_roman']}", # We can enhance this if we have titles in json
                    "subtitle": desc.get("subtitle"),
                    "description": desc.get("description")
                }
            
            generate_heath_rst(
                book_data, 
                output_dir, 
                graph, 
                ref_to_path_map, 
                metadata
            )
            
        except Exception as e:
            print(f"Error processing {xml_file.name}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
