import json
import re
from pathlib import Path

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def normalize_label(label):
    # Handle Roman numeral I -> 1 for the first prop
    if label.strip() == "I":
        return "1"
    return label.strip()

def find_image_path(base_dir, volume, page_num):
    vol_dir = base_dir / f"volume_{volume}"
    filename = f"{page_num:04d}.png"
    # Search recursively in the volume directory
    found = list(vol_dir.rglob(filename))
    if found:
        return found[0].relative_to(base_dir)
    return None

def get_book_roman(book_slug):
    # book_i -> I, book_ii -> II, etc.
    # Simple mapping or parsing
    mapping = {
        "book_i": "I", "booki": "I",
        "book_ii": "II", "bookii": "II",
        "book_iii": "III", "bookiii": "III",
        "book_iv": "IV", "bookiv": "IV",
        "book_v": "V", "bookv": "V",
        "book_vi": "VI", "bookvi": "VI",
        "book_vii": "VII", "bookvii": "VII",
        "book_viii": "VIII", "bookviii": "VIII",
        "book_ix": "IX", "bookix": "IX",
        "book_x": "X", "bookx": "X",
        "book_xi": "XI", "bookxi": "XI",
        "book_xii": "XII", "bookxii": "XII",
        "book_xiii": "XIII", "bookxiii": "XIII"
    }
    return mapping.get(book_slug, book_slug)

def generate_index():
    heath_dir = Path("resources/heath")
    manual_dir = Path("resources/heath_manual")
    
    old_index_path = heath_dir / "proposition_index.json"
    instructions_path = manual_dir / "cropping_instructions.json"
    
    old_index = load_json(old_index_path)
    instructions = load_json(instructions_path)
    
    new_index = {}
    
    # Handle list vs dict input
    if isinstance(old_index, list):
        items = old_index
    else:
        items = old_index.values()
        
    print(f"Processing {len(items)} propositions...")
    
    for item in items:
        vol = item['volume']
        book_slug = item['book']
        book_roman = get_book_roman(book_slug)
        
        # Handle 'label' (old) vs 'proposition' (new)
        raw_label = item.get('label') or item.get('proposition')
        label = normalize_label(raw_label)
        
        canonical_id = f"{book_roman}.{label}"
        
        # Start building the new entry
        entry = {
            "id": canonical_id,
            "volume": vol,
            "book": book_slug,
            "proposition": label,
            "start_page": item['start_page'],
            "end_page": item['end_page'],
            "pages": item.get('pages', []),     # Preserve existing if present
            "graphics": item.get('graphics', []) # Preserve existing if present
        }
        
        # If we are reprocessing, we might want to re-check instructions 
        # to ensure we have the latest crop info if it changed or if ID changed.
        # The ID might have changed from "I.1" (ambiguous) to "II.1".
        # So we should look up instructions using the NEW canonical ID.
        
        # Reset pages/graphics if we are re-fetching from instructions
        # But if instructions don't exist, keep what we have?
        # Actually, we want to re-generate the pages list if we can, to ensure correctness.
        
        crop_info = instructions.get(canonical_id)
        
        if crop_info:
            # Re-populate pages from instructions
            entry['pages'] = []
            entry['graphics'] = []
            
            current_page = item['start_page']
            instr_pages = crop_info.get('pages', [])
            
            for p_instr in instr_pages:
                # Resolve file path
                rel_path = find_image_path(heath_dir, vol, current_page)
                
                page_entry = {
                    "page": current_page,
                    "file": str(rel_path) if rel_path else None,
                    "start_offset": p_instr.get('start_offset', 0),
                    "end_offset": p_instr.get('end_offset', 0)
                }
                entry['pages'].append(page_entry)
                current_page += 1
            
            entry['graphics'] = [{
                "x_offset": crop_info.get('graphic_x_offset'),
                "y_offset": crop_info.get('graphic_y_offset'),
                "crop_box": crop_info.get('graphic_crop_box')
            }]
        
        elif not entry['pages']:
             # If no pages yet (fresh from old list) and no instructions
            for p in range(item['start_page'], item['end_page'] + 1):
                rel_path = find_image_path(heath_dir, vol, p)
                entry['pages'].append({
                    "page": p,
                    "file": str(rel_path) if rel_path else None
                })
                
        new_index[canonical_id] = entry

    # Write the new index
    # Convert dict to sorted list or keep dict? 
    # The previous one was a list. A dict keyed by ID is often more useful, 
    # but if we want to preserve order, we might want a list.
    # The user said "label the proposition with the canonical id". 
    # A dict { "I.1": { ... } } is cleaner for lookups.
    
    output_path = heath_dir / "proposition_index.json"
    with open(output_path, 'w') as f:
        json.dump(new_index, f, indent=2)
        
    print(f"Generated new index with {len(new_index)} entries at {output_path}")

if __name__ == "__main__":
    generate_index()
