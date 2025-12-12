import cv2
import json
import argparse
import numpy as np
from pathlib import Path
import sys

# Configuration
HEATH_DIR = Path("resources/heath")

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def get_book_slug_from_path(path):
    # path is like .../volume_I/book_i/propositions/index.json
    try:
        # parent is propositions, parent.parent is book_i
        return path.parent.parent.name
    except:
        return None

def detect_graphic_cv(image_path, debug=False):
    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        return {"error": "Could not load image"}
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Binarize (Invert so ink is white, paper is black)
    # Otsu's thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 2. Connected Components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    
    graphics_mask = np.zeros_like(binary)
    
    large_components = []
    
    # Thresholds
    MIN_GRAPHIC_DIM = 60   # Minimum width or height to be considered a "line" or "circle" part
    MAX_TEXT_HEIGHT = 40   # Height of a line of text usually < 30-40px
    MIN_TEXT_WIDTH = 100   # Lines of text are usually wider than this
    
    # Step A: Find the "Core" (the actual drawing)
    for i in range(1, num_labels): # Skip background
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        
        # Filter text lines
        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue 
            
        if w > MIN_GRAPHIC_DIM or h > MIN_GRAPHIC_DIM:
            large_components.append(i)
            graphics_mask[labels == i] = 255
            
    if not large_components:
        return {"error": "No large graphic components found"}
        
    # Step B: Bounding box of the core
    points = cv2.findNonZero(graphics_mask)
    if points is None:
         return {"error": "Mask empty"}
         
    gx, gy, gw, gh = cv2.boundingRect(points)
    
    # Step C: Add nearby labels (points, letters)
    LABEL_SEARCH_MARGIN = 20  
    
    search_x = max(0, gx - LABEL_SEARCH_MARGIN)
    search_y = max(0, gy - LABEL_SEARCH_MARGIN)
    search_w = gw + 2*LABEL_SEARCH_MARGIN
    search_h = gh + 2*LABEL_SEARCH_MARGIN
    
    final_mask = graphics_mask.copy()
    
    for i in range(1, num_labels):
        if i in large_components:
            continue
            
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        
        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue
            
        cx = x + w/2
        cy = y + h/2
        
        if (search_x <= cx <= search_x + search_w) and (search_y <= cy <= search_y + search_h):
            final_mask[labels == i] = 255
            
    points = cv2.findNonZero(final_mask)
    if points is None:
        return {"error": "Final mask empty"}

    gx, gy, gw, gh = cv2.boundingRect(points)
    
    # Padding
    PADDING = 10
    height, width = img.shape[:2]
    
    gx = max(0, gx - PADDING)
    gy = max(0, gy - PADDING)
    gw = min(width - gx, gw + 2*PADDING)
    gh = min(height - gy, gh + 2*PADDING)
    
    if debug:
        debug_dir = Path("debug_graphics")
        debug_dir.mkdir(exist_ok=True)
        debug_img = img.copy()
        cv2.rectangle(debug_img, (gx, gy), (gx + gw, gy + gh), (0, 0, 255), 2)
        debug_path = debug_dir / f"{Path(image_path).name}"
        cv2.imwrite(str(debug_path), debug_img)

    return {
        "x_offset": int(gx),
        "y_offset": int(gy),
        "crop_box": [int(gw), int(gh)]
    }

def process_books(target_book=None, dry_run=False, debug=False):
    # Find all index files
    index_files = sorted(HEATH_DIR.rglob("volume_*/book_*/propositions/index.json"))
    
    if not index_files:
        print("No index.json files found.")
        return

    for index_path in index_files:
        book_slug = get_book_slug_from_path(index_path)
        
        # Filter by book if requested
        if target_book:
            t_book = target_book.lower()
            b_slug = book_slug.lower()
            
            match = False
            if t_book == b_slug: match = True
            if f"book_{t_book}" == b_slug: match = True
            if f"book{t_book}" == b_slug: match = True
            
            if not match:
                continue

        print(f"Processing {book_slug}...")
        propositions = load_json(index_path)
        updated_count = 0
        
        for prop in propositions:
            prop_id = prop['id']
            image_path = HEATH_DIR / "propositions" / f"{prop_id}.png"
            
            if not image_path.exists():
                print(f"  Skipping {prop_id}: Image not found")
                continue
                
            result = detect_graphic_cv(image_path, debug=debug)
            
            if "error" in result:
                print(f"  {prop_id}: {result['error']}")
            else:
                prop['graphics'] = [result]
                updated_count += 1
                print(f"  {prop_id}: Updated {result}")

        if not dry_run:
            save_json(index_path, propositions)
            print(f"Saved {updated_count} updates to {index_path}")
        else:
            print(f"Dry run: would have saved {updated_count} updates.")

def main():
    parser = argparse.ArgumentParser(description="Scan and update graphic coordinates using OpenCV.")
    parser.add_argument("--book", "-b", type=str, help="Specific book to scan (e.g., 'I' or 'book_i').")
    parser.add_argument("--dry-run", action="store_true", help="Do not save changes")
    parser.add_argument("--debug", action="store_true", help="Save debug images to debug_graphics/ folder")
    
    args = parser.parse_args()
    
    process_books(args.book, args.dry_run, args.debug)

if __name__ == "__main__":
    main()