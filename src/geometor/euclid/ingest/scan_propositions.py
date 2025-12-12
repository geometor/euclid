import json
import re
import argparse
from pathlib import Path

# Configuration
HEATH_DIR = Path("resources/heath")
CROPPING_INSTRUCTIONS = Path("resources/heath_manual/cropping_instructions.json")

DEFAULT_PAGE_HEIGHT = 1200
PAGE_HEADER_END = 125
PAGE_FOOTER_START = 1115
BODY_HEIGHT = PAGE_FOOTER_START - PAGE_HEADER_END

# Roman to Arabic for Book numbers (if needed) or just use directory names
BOOK_MAP = {
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

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def get_book_and_volume_from_path(file_path):
    parts = Path(file_path).relative_to(HEATH_DIR).parts
    volume_key = None
    book_slug = None
    
    for p in parts:
        if p.startswith("volume_"):
            volume_key = p.replace("volume_", "").upper()
        if p.startswith("book_") or p.startswith("book"):
            book_slug = p.lower()
            
    return volume_key, book_slug

def scan_propositions(target_book=None):
    print("""
    ----------------------------------------------------------------------------------------------------
    WARNING: Running this script may overwrite manual cleanup, QED/QEF markers, and proposition index tweaks.
    If you are sure you want to proceed, comment out the 'return' statement below this warning.
    ----------------------------------------------------------------------------------------------------
    """)
    return
    
    cropping_data = load_json(CROPPING_INSTRUCTIONS)
    
    # We will now organize propositions by book to save individual indexes
    # Structure: { (vol_key, book_slug): [prop_list] }
    propositions_by_book = {}
    book_proposition_counters = {} # To keep track of proposition numbers per book
    
    prop_text_files = sorted(HEATH_DIR.rglob("volume_*/book_*/propositions/*.txt"))
    
    files_by_book = {}
    for f_path in prop_text_files:
        vol_key, book_slug = get_book_and_volume_from_path(f_path)
        if vol_key and book_slug:
            # Filter if target_book is specified
            # Check against book_slug (e.g., "book_i") or mapped Roman (e.g., "I")
            book_roman = BOOK_MAP.get(book_slug, book_slug)
            
            if target_book:
                # Normalize target book to check against slug or Roman
                t_book = target_book.lower()
                if t_book != book_slug and t_book != book_roman.lower():
                    continue

            key = (vol_key, book_slug)
            if key not in files_by_book:
                files_by_book[key] = []
            files_by_book[key].append(f_path)
            
    if not files_by_book:
        print(f"No files found for book: {target_book}")
        return

    for (vol_key, book_slug), files in files_by_book.items():
        book_roman = BOOK_MAP.get(book_slug, book_slug)
        prop_counter = book_proposition_counters.get(book_roman, 0)
        current_prop = None
        
        if (vol_key, book_slug) not in propositions_by_book:
            propositions_by_book[(vol_key, book_slug)] = []

        print(f"Scanning {vol_key}/{book_slug}...")

        # Store all lines for this book to easily calculate offsets for any page
        book_lines_by_page = {}
        for f_path in files:
            page_num = int(re.search(r'(\d{4})\.txt$', f_path.name).group(1)) if re.search(r'(\d{4})\.txt$', f_path.name) else 0
            try:
                with open(f_path, 'r') as f:
                    book_lines_by_page[page_num] = f.readlines()
            except Exception as e:
                print(f"Error reading {f_path}: {e}")
                book_lines_by_page[page_num] = []

        for f_idx, f_path in enumerate(files):
            page_num = int(re.search(r'(\d{4})\.txt$', f_path.name).group(1)) if re.search(r'(\d{4})\.txt$', f_path.name) else 0
            lines = book_lines_by_page[page_num]
            total_lines = len(lines)
            
            for i, line in enumerate(lines):
                line_stripped = line.strip()
                
                is_proposition_start = re.match(r'^PROPOSITION\s*$', line_stripped, re.IGNORECASE)
                is_proposition_end = re.match(r'^Q\.\s*E\.\s*D\.$|^Q\.\s*E\.\s*F\.$|^\(Being\) what it was required to do\.$', line_stripped, re.IGNORECASE)

                if is_proposition_start:
                    # If a new proposition starts, close the previous one first
                    if current_prop and current_prop['status'] == 'open':
                        current_prop['end_page'] = page_num
                        current_prop['end_line_index'] = i - 1
                        current_prop['end_line_text'] = lines[i-1].strip() if i > 0 else ""
                        current_prop['status'] = 'closed_by_next_prop_start'

                        cut_y = int(PAGE_HEADER_END + (i / total_lines) * BODY_HEIGHT) if total_lines > 0 else PAGE_FOOTER_START
                        end_offset_val = DEFAULT_PAGE_HEIGHT - cut_y

                        if current_prop['pages'] and current_prop['pages'][-1]['page'] == page_num:
                            current_prop['pages'][-1]['end_offset_px'] = end_offset_val
                        else:
                            current_prop['pages'].append({
                                "page": page_num,
                                "file": str(HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions" / f"{page_num:04d}.png"),
                                "start_offset_px": PAGE_HEADER_END,
                                "end_offset_px": end_offset_val
                            })

                    prop_counter += 1
                    canonical_id = f"{book_roman}.{prop_counter}"
                    
                    current_prop = {
                        "id": canonical_id,
                        "volume": vol_key,
                        "book": book_slug,
                        "proposition_number": prop_counter,
                        "start_page": page_num,
                        "start_line_index": i,
                        "start_line_text": line_stripped,
                        "end_page": None,
                        "end_line_index": None,
                        "status": "open",
                        "pages": [], 
                        "graphics": []
                    }
                    # Add to current book list instead of global dict
                    propositions_by_book[(vol_key, book_slug)].append(current_prop)
                    
                    start_y = int(PAGE_HEADER_END + (i / total_lines) * BODY_HEIGHT) if total_lines > 0 else PAGE_HEADER_END
                    
                    current_prop['pages'].append({
                        "page": page_num,
                        "file": str(HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions" / f"{page_num:04d}.png"),
                        "start_offset_px": start_y,
                        "end_offset_px": DEFAULT_PAGE_HEIGHT - PAGE_FOOTER_START 
                    })

                elif current_prop and is_proposition_end:
                    current_prop['end_page'] = page_num
                    current_prop['end_line_index'] = i
                    current_prop['end_line_text'] = line_stripped
                    current_prop['status'] = 'closed_by_qed'
                    
                    cut_y = int(PAGE_HEADER_END + ((i + 1) / total_lines) * BODY_HEIGHT) if total_lines > 0 else PAGE_FOOTER_START
                    end_offset_val = DEFAULT_PAGE_HEIGHT - cut_y

                    if current_prop['pages'] and current_prop['pages'][-1]['page'] == page_num:
                        current_prop['pages'][-1]['end_offset_px'] = end_offset_val
                    else: 
                        current_prop['pages'].append({
                            "page": page_num,
                            "file": str(HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions" / f"{page_num:04d}.png"),
                            "start_offset_px": PAGE_HEADER_END,
                            "end_offset_px": end_offset_val
                        })
                    current_prop = None 
                
            if current_prop and current_prop['status'] == 'open':
                if not current_prop['pages'] or current_prop['pages'][-1]['page'] != page_num:
                    if current_prop['start_page'] != page_num:
                        current_prop['pages'].append({
                            "page": page_num,
                            "file": str(HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions" / f"{page_num:04d}.png"),
                            "start_offset_px": PAGE_HEADER_END,
                            "end_offset_px": DEFAULT_PAGE_HEIGHT - PAGE_FOOTER_START 
                        })

        if current_prop and current_prop['status'] == 'open':
            last_file_in_book = files[-1]
            last_page_num = int(re.search(r'(\d{4})\.txt$', last_file_in_book.name).group(1))
            last_lines = book_lines_by_page.get(last_page_num, [])
            
            current_prop['end_page'] = last_page_num
            current_prop['end_line_index'] = len(last_lines) - 1
            current_prop['end_line_text'] = last_lines[-1].strip() if last_lines else ""
            current_prop['status'] = 'closed_by_end_of_book'

            end_offset_val = DEFAULT_PAGE_HEIGHT - PAGE_FOOTER_START

            if current_prop['pages'] and current_prop['pages'][-1]['page'] == last_page_num:
                current_prop['pages'][-1]['end_offset_px'] = end_offset_val
            else:
                start_offset_px = PAGE_HEADER_END
                if current_prop['start_page'] == last_page_num:
                    start_y = int(PAGE_HEADER_END + (current_prop['start_line_index'] / len(last_lines)) * BODY_HEIGHT) if len(last_lines) > 0 else PAGE_HEADER_END
                    start_offset_px = start_y

                current_prop['pages'].append({
                    "page": last_page_num,
                    "file": str(HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions" / f"{last_page_num:04d}.png"),
                    "start_offset_px": start_offset_px,
                    "end_offset_px": end_offset_val
                })
        
        book_proposition_counters[book_roman] = prop_counter
    
    # Final pass to merge cropping data and add placeholders, then save PER BOOK
    PLACEHOLDER_GRAPHIC = {
        "x_offset": 335,
        "y_offset": 130,
        "crop_box": [300, 200]
    }

    for (vol_key, book_slug), props_list in propositions_by_book.items():
        final_propositions_list = []
        for prop in props_list:
            canonical_id = prop['id']
            if canonical_id in cropping_data:
                c_info = cropping_data[canonical_id]
                prop['graphics'] = [{
                    "x_offset": c_info.get('graphic_x_offset'),
                    "y_offset": c_info.get('graphic_y_offset'),
                    "crop_box": c_info.get('graphic_crop_box')
                }]
            else:
                prop['graphics'] = [PLACEHOLDER_GRAPHIC]
            final_propositions_list.append(prop)

        # Construct path: resources/heath/volume_X/book_y/propositions/index.json
        # We need to ensure the directory exists.
        # Note: scan found .txt files in .../propositions/*.txt, so the directory should exist.
        book_props_dir = HEATH_DIR / f"volume_{vol_key}" / book_slug / "propositions"
        book_props_dir.mkdir(parents=True, exist_ok=True)
        output_index_path = book_props_dir / "index.json"
        
        with open(output_index_path, 'w') as f:
            json.dump(final_propositions_list, f, indent=2)
            
        print(f"Generated {output_index_path} with {len(final_propositions_list)} propositions.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan propositions from text files.")
    parser.add_argument("--book", "-b", type=str, help="Specific book to scan (e.g., 'I' or 'book_i'). If omitted, scans all found books.")
    args = parser.parse_args()
    
    scan_propositions(target_book=args.book)
