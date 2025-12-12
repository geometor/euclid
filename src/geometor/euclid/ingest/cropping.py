import json
import os
from PIL import Image
from pathlib import Path
from geometor.elements.ingest.config import (
    PROPOSITION_INDEX_PATH, 
    EXTRACTED_DIR,
    RESOURCES_DIR,
    VOLUMES,
    PAGE_WIDTH,
    PAGE_HEADER_END,
    PAGE_FOOTER_START,
    CROP_WIDTH
)
from geometor.elements.ingest.utils import load_json

CROPPED_DIR = EXTRACTED_DIR / "cropped"

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def calculate_crop_box(img_height, total_lines, start_line=0, end_line=None):
    """
    Calculates the crop box based on line indices.
    Assumes linear distribution of lines within the text area.
    """
    # The active text area on the page
    text_area_height = PAGE_FOOTER_START - PAGE_HEADER_END
    
    if total_lines == 0:
        return (0, 0, 0, 0) # Should not happen

    px_per_line = text_area_height / total_lines
    
    # Calculate top Y
    if start_line > 0:
        # We add some padding (e.g., 1-2 lines) above the start line to be safe
        # But strictly, start_line * px_per_line is the distance from top of text area
        top_offset = (start_line * px_per_line)
        # Adjust relative to page
        top_y = PAGE_HEADER_END + top_offset
    else:
        top_y = PAGE_HEADER_END
        
    # Calculate bottom Y
    if end_line is not None:
        # end_line is the index of the last line. 
        # So we want to include it.
        bottom_offset = ((end_line + 1) * px_per_line)
        bottom_y = PAGE_HEADER_END + bottom_offset
    else:
        bottom_y = PAGE_FOOTER_START

    # Centered horizontal crop
    left_x = (PAGE_WIDTH - CROP_WIDTH) // 2
    right_x = left_x + CROP_WIDTH
    
    # Ensure bounds
    top_y = max(0, top_y)
    bottom_y = min(img_height, bottom_y)
    
    # Add a small padding/margin if we calculated dynamic coords
    # (Only if not hitting the hard header/footer limits)
    if start_line > 0:
        top_y = max(PAGE_HEADER_END, top_y - 10) 
    if end_line is not None:
        bottom_y = min(PAGE_FOOTER_START, bottom_y + 10)

    return (left_x, top_y, right_x, bottom_y)

def process_propositions():
    """
    Automated cropping of propositions based on analysis data.
    """
    print("""
    ----------------------------------------------------------------------------------------------------
    WARNING: Running this script may overwrite manual cleanup, QED/QEF markers, and proposition index tweaks.
    If you are sure you want to proceed, comment out the 'return' statement below this warning.
    ----------------------------------------------------------------------------------------------------
    """)
    return

    propositions = load_json(PROPOSITION_INDEX_PATH)
    
    # Load manual instructions ONLY for graphics for now
    manual_instructions_path = RESOURCES_DIR / "heath_manual" / "cropping_instructions.json"
    manual_instructions = {}
    if manual_instructions_path.exists():
        manual_instructions = load_json(manual_instructions_path)
    
    if not propositions:
        print("Error loading proposition index.")
        return

    # Create a lookup map for page images: { "volume_I_255": "path/to/image.png" }
    # Paths will be relative to the volume directory
    page_lookup = {}
    for vol_key in VOLUMES.keys():
        manifest_path = EXTRACTED_DIR / f"volume_{vol_key}" / "pages.json"
        manifest = load_json(manifest_path)
        if not manifest:
            print(f"Warning: No manifest found for {vol_key}")
            continue
            
        for page_info in manifest.get("pages", []):
            p_num = page_info.get("page_num")
            # Store relative path from EXTRACTED_DIR / volume_X
            # e.g. "book_i/0001.png"
            # Key format: volume_I_255
            page_lookup[f"volume_{vol_key}_{p_num}"] = page_info.get("image")

    ensure_dir(CROPPED_DIR)
    
    # Helper to extract Roman numeral from book string "book_i", "book_ii"
    def get_book_numeral(book_str):
        # Assumes format "book_x" where x is roman numeral or word
        if not book_str: return "I" # Fallback
        parts = book_str.split('_')
        if len(parts) > 1:
            return parts[1].upper()
        return "I"

    print(f"Processing {len(propositions)} propositions...")

    for prop in propositions:
        vol = prop['volume']
        book_slug = prop.get('book', 'book_i')
        book_numeral = get_book_numeral(book_slug)
        
        label = prop['label']
        normalized_label = "1" if label == "I" else label
        
        # Key format: BOOK.PROP (e.g. I.1, II.5)
        # This is used for the output filename
        prop_key = f"{book_numeral}.{normalized_label}"
        
        # Determine pages
        start_page = prop['start_page']
        end_page = prop['end_page']
        
        if end_page is None:
            # Proposition might be incomplete or single page at end of book
            page_range = [start_page]
        else:
            page_range = list(range(start_page, end_page + 1))
            
        cropped_images = []
        
        for i, page_num in enumerate(page_range):
            # Lookup image using Volume (physical location)
            # Key format: volume_I_255
            vol_key = f"volume_{vol}"
            lookup_key = f"{vol_key}_{page_num}"
            rel_img_path = page_lookup.get(lookup_key)
            
            if not rel_img_path:
                print(f"  Missing image for {prop_key} page {page_num} (key: {lookup_key})")
                cropped_images = []
                break
                
            # EXTRACTED_DIR / volume_X / rel_img_path
            input_path = EXTRACTED_DIR / vol_key / rel_img_path
            
            if not input_path.exists():
                 print(f"  Image file not found: {input_path}")
                 cropped_images = []
                 break
                 
            try:
                img = Image.open(input_path)
                
                # Determine start/end lines for this page
                p_start_line = 0
                p_end_line = None # Means go to footer
                
                # If this is the first page of the prop
                if i == 0:
                    p_start_line = prop['start_line_index']
                    
                # If this is the last page of the prop
                if i == len(page_range) - 1:
                    if prop['end_line_index'] is not None:
                        p_end_line = prop['end_line_index']
                
                # Total lines on THIS page
                current_total_lines = 40 # Default fallback
                
                if i == 0:
                    current_total_lines = prop['start_page_total_lines']
                elif i == len(page_range) - 1 and prop['end_page_total_lines']:
                    current_total_lines = prop['end_page_total_lines']
                else:
                    # Middle page
                    pass

                box = calculate_crop_box(img.height, current_total_lines, p_start_line, p_end_line)
                
                # Validate box
                if box[2] <= box[0] or box[3] <= box[1]:
                    print(f"  Invalid crop box {box} for {prop_key} page {page_num}")
                    cropped_images = []
                    break
                    
                cropped_images.append(img.crop(box))
                
            except Exception as e:
                print(f"  Error processing {prop_key}: {e}")
                cropped_images = []
                break
        
        if not cropped_images:
            continue
            
        # Stitch
        if len(cropped_images) > 1:
            total_height = sum(img.height for img in cropped_images)
            stitched_image = Image.new('RGB', (CROP_WIDTH, total_height), (255, 255, 255))
            current_y = 0
            for img in cropped_images:
                stitched_image.paste(img, (0, current_y))
                current_y += img.height
        else:
            stitched_image = cropped_images[0]
            
        output_filename = f"{prop_key}.png"
        stitched_image.save(CROPPED_DIR / output_filename)
        
        # Graphic Extraction (Manual Fallback)
        # The manual instructions use keys like "I.1".
        # If our prop_key matches, we can try to extract the graphic.
        if prop_key in manual_instructions:
             instr = manual_instructions[prop_key]
             gx = instr.get("graphic_x_offset")
             gy = instr.get("graphic_y_offset")
             g_box = instr.get("graphic_crop_box")
             
             if all([gx is not None, gy is not None, g_box is not None]):
                 graphic_width, graphic_height = g_box
                 graphic_box = (gx, gy, gx + graphic_width, gy + graphic_height)
                 
                 if graphic_box[2] <= stitched_image.width and graphic_box[3] <= stitched_image.height:
                     graphic_img = stitched_image.crop(graphic_box)
                     graphic_img.save(CROPPED_DIR / f"{prop_key}.graphic.png")

def run_cropping():
    process_propositions()
