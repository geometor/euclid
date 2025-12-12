import cv2
import json
import argparse
import numpy as np
from pathlib import Path
import os

# Configuration
HEATH_DIR = Path("resources/heath")
PROPOSITIONS_DIR = HEATH_DIR / "propositions"
INDEX_PATH = HEATH_DIR / "volume_I/book_i/propositions/index.json"

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def detect_graphic_cv(image_path, debug=False):
    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        return {"error": "Could not load image"}
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Binarize (Invert so ink is white, paper is black)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 2. Connected Components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    
    graphics_mask = np.zeros_like(binary)
    
    # GROUPS
    # 1. Core Graphic: Large connected parts (lines, circles)
    # 2. Labels: Small parts near the core
    # 3. Text: Wide, short parts (we want to avoid these)
    
    large_components = []
    
    # Thresholds
    MIN_GRAPHIC_DIM = 60   # Minimum width or height to be considered a "line" or "circle" part
    MAX_TEXT_HEIGHT = 40   # Height of a line of text usually < 30-40px
    MIN_TEXT_WIDTH = 100   # Lines of text are usually wider than this
    
    # Step A: Find the "Core" (the actual drawing)
    for i in range(1, num_labels): # Skip background
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        
        # If it's big enough in either dimension, it's likely part of the drawing.
        # But if it's WIDE and SHORT, it's a text line -> Ignore it.
        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue # This is a line of text
            
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
    # We search for small components near the core rect, BUT we filter out text lines.
    
    LABEL_SEARCH_MARGIN = 20  # How far from the graphic to look for labels (tightened from 50)
    
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
        
        # Filter: Is this component a line of text?
        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue
            
        # Center of component
        cx = x + w/2
        cy = y + h/2
        
        # Check proximity
        if (search_x <= cx <= search_x + search_w) and (search_y <= cy <= search_y + search_h):
            final_mask[labels == i] = 255
            
    # Recalculate bounding box
    points = cv2.findNonZero(final_mask)
    gx, gy, gw, gh = cv2.boundingRect(points)
    
    # Add a small aesthetic padding to the final crop
    PADDING = 10
    height, width = img.shape[:2]
    
    gx = max(0, gx - PADDING)
    gy = max(0, gy - PADDING)
    gw = min(width - gx, gw + 2*PADDING)
    gh = min(height - gy, gh + 2*PADDING)
    
    if debug:
        # Draw rectangle and save debug image
        debug_img = img.copy()
        cv2.rectangle(debug_img, (gx, gy), (gx + gw, gy + gh), (0, 0, 255), 2)
        debug_path = f"debug_{Path(image_path).name}"
        cv2.imwrite(debug_path, debug_img)
        print(f"Saved debug image to {debug_path}")

    return {
        "x_offset": int(gx),
        "y_offset": int(gy),
        "crop_box": [int(gw), int(gh)]
    }

def run_test():
    print("Running OpenCV Graphic Detection Test")
    propositions = load_json(INDEX_PATH)
    prop_map = {p['id']: p for p in propositions}
    
    target_props = ["I.1", "I.2", "I.3"]
    
    for prop_id in target_props:
        print(f"\nProcessing {prop_id}...")
        prop_data = prop_map.get(prop_id)
        
        # Ground Truth
        gt_graphics = prop_data.get('graphics', [{}])[0]
        print(f"  Ground Truth: {gt_graphics}")
        
        image_path = PROPOSITIONS_DIR / f"{prop_id}.png"
        if not image_path.exists():
            print("  Image not found")
            continue
            
        result = detect_graphic_cv(image_path, debug=True)
        print(f"  CV Detected:  {result}")
        
        if "error" not in result:
            gt_x = gt_graphics.get('x_offset', 0)
            gt_y = gt_graphics.get('y_offset', 0)
            gt_w, gt_h = gt_graphics.get('crop_box', [0, 0])
            
            d_x = result['x_offset'] - gt_x
            d_y = result['y_offset'] - gt_y
            d_w = result['crop_box'][0] - gt_w
            d_h = result['crop_box'][1] - gt_h
            
            print(f"  Diff (CV - GT): x={d_x:+d}, y={d_y:+d}, w={d_w:+d}, h={d_h:+d}")

if __name__ == "__main__":
    run_test()
