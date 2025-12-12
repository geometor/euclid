import json
import os
import argparse
from pathlib import Path
from PIL import Image
from geometor.elements.ingest.cleanup import clean_image

# Configuration
HEATH_DIR = Path("resources/heath")

# Constants
PAGE_WIDTH = 755
CROP_WIDTH = 640

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def get_book_slug_from_path(path):
    # path is like .../volume_I/book_i/propositions/index.json
    # return "book_i"
    try:
        # parent is propositions, parent.parent is book_i
        return path.parent.parent.name
    except:
        return None

def stitch_propositions(target_book=None):
    
    # Find all index files
    index_files = sorted(HEATH_DIR.rglob("volume_*/book_*/propositions/index.json"))
    
    if not index_files:
        print("No index.json files found in book directories. Did you run scan_propositions.py?")
        return

    print(f"Found {len(index_files)} index files.")
    
    for index_path in index_files:
        book_slug = get_book_slug_from_path(index_path)
        
        # Filter by book if requested
        if target_book:
            # Check if target matches book_slug (book_i) or is contained (I in book_i?? no, strict check or map)
            # Let's assume strict matching or simple containment for flexibility
            # If user says "I", we match "book_i". User says "book_i", match "book_i".
            
            # Simple heuristic: target in slug or slug in target? 
            # Better: Normalize.
            t_book = target_book.lower()
            b_slug = book_slug.lower()
            
            # If target is "I", we need to know if book_slug is "book_i".
            # Let's use the same map or just rudimentary checking.
            # Actually, let's just check if the target string appears in the slug.
            # "i" is in "book_i", "book_ii", "book_iii". Bad.
            # "book_i" == "book_i".
            # "I" -> "book_i"?
            
            # Let's rely on the user providing "book_i" or "I" if we can map it.
            # Since I don't have the map here, I'll just check for exact slug match OR "book_"+target == slug
            match = False
            if t_book == b_slug: match = True
            if f"book_{t_book}" == b_slug: match = True
            if f"book{t_book}" == b_slug: match = True
            
            if not match:
                continue

        print(f"Processing index: {index_path} (Book: {book_slug})")
        propositions = load_json(index_path)
        
        # Determine output directory for cropped images.
        # Previously: resources/heath/propositions (flat).
        # Now: Should probably be per book? User didn't explicitly say "move cropped images to per-book folder", 
        # but said "store the indexes in the propositions folders" and "restitching all 13 books... is daunting".
        # If I put cropped images in the book folder, it's cleaner. 
        # "propositions" folder in the book directory seems like the right place for the *source* pages?
        # Wait, the source pages are already in `volume_I/book_i/propositions/*.png`.
        # The `scan_propositions` script refers to source pages as `file: .../propositions/0001.png`.
        
        # The `stitch` script previously output to `HEATH_DIR / "propositions"`.
        # If I change this, I change the project structure significantly.
        # The user asked to "scan and stitch on a book by book basis".
        # If I stick to the global output folder, I can still just run for one book and update those files.
        # However, storing indexes locally suggests a move towards locality.
        # But the global `graphics` and `propositions` folders might be expected by other tools (like Sphinx build).
        # I'll stick to the existing output directories for the IMAGES to be safe, unless "propositions" folder in the book dir was meant for the output?
        # The input pages are in `propositions` folder of the book.
        # If I write output to the same folder, it mixes source pages and result clips.
        # Let's keep the output in the global `resources/heath/propositions` and `resources/heath/graphics` for now, 
        # just restricted to the book being processed.
        
        CROPPED_DIR = HEATH_DIR / "propositions"
        ensure_dir(CROPPED_DIR)

        for prop in propositions:
            prop_id = prop['id']
            
            cropped_segments = []
            
            for page_info in prop['pages']:
                file_rel_path = page_info['file']
                input_path = HEATH_DIR / file_rel_path
                
                # Fix path if it's absolute-ish or double relative
                # The scan script puts: "resources/heath/volume_..."
                # HEATH_DIR is "resources/heath"
                # if file_rel_path starts with resources/heath, we should strip it or use project root.
                if str(file_rel_path).startswith("resources/heath"):
                     input_path = Path(file_rel_path)
                
                if not input_path.exists():
                    # Try relative to project root
                    if Path(file_rel_path).exists():
                        input_path = Path(file_rel_path)
                    else:
                        # print(f"  Error: Image not found: {file_rel_path}")
                        continue
                
                try:
                    img = Image.open(input_path)
                    
                    start_px = page_info['start_offset_px']
                    end_margin_px = page_info['end_offset_px']
                    
                    top = start_px
                    bottom = img.height - end_margin_px
                    
                    img_width = img.width
                    left = (img_width - CROP_WIDTH) // 2
                    right = left + CROP_WIDTH
                    
                    if top >= bottom:
                        continue
                    
                    if left < 0: left = 0
                    if right > img_width: right = img_width
                    
                    crop_box = (left, top, right, bottom)
                    segment = img.crop(crop_box)
                    
                    # Apply cleanup (bleed removal)
                    segment = clean_image(segment, white_point=226)
                    
                    cropped_segments.append(segment)
                    
                except Exception as e:
                    print(f"  Error processing image {input_path}: {e}")
            
            if not cropped_segments:
                # print(f"  No segments for {prop_id}. Skipping.")
                continue
                
            total_height = sum(seg.height for seg in cropped_segments)
            max_width = max(seg.width for seg in cropped_segments)
            
            stitched_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))
            
            current_y = 0
            for seg in cropped_segments:
                x_offset = (max_width - seg.width) // 2
                stitched_image.paste(seg, (x_offset, current_y))
                current_y += seg.height
                
            output_filename = f"{prop_id}.png"
            stitched_image.save(CROPPED_DIR / output_filename)
            
            if 'graphics' in prop and prop['graphics']:
                g_info = prop['graphics'][0]
                gx = g_info.get('x_offset')
                gy = g_info.get('y_offset')
                g_box = g_info.get('crop_box')
                
                if gx is not None and gy is not None and g_box:
                    gw, gh = g_box
                    
                    if gx + gw <= stitched_image.width and gy + gh <= stitched_image.height:
                        graphic_crop = (gx, gy, gx + gw, gy + gh)
                        graphic_img = stitched_image.crop(graphic_crop)
                        graphic_img.save(CROPPED_DIR / f"{prop_id}.graphic.png")
                    else:
                        pass

    print(f"Stitching complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stitch propositions from scanned indexes.")
    parser.add_argument("--book", "-b", type=str, help="Specific book to stitch (e.g., 'I' or 'book_i').")
    args = parser.parse_args()
    
    stitch_propositions(target_book=args.book)
