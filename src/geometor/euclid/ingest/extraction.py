import os
import subprocess
import glob
import shutil
import xml.etree.ElementTree as ET
import json
from pathlib import Path
from geometor.elements.ingest.config import PDF_BASE_DIR, EXTRACTED_DIR, VOLUMES

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def extract_volume(vol_key, relative_path):
    pdf_path = PDF_BASE_DIR / relative_path
    if not pdf_path.exists():
        print(f"Error: PDF not found for Volume {vol_key} at {pdf_path}")
        return

    vol_output_dir = EXTRACTED_DIR / f"volume_{vol_key}"
    ensure_dir(vol_output_dir)
    
    print(f"Processing Volume {vol_key}...")
    print(f"  PDF: {pdf_path}")
    print(f"  Output: {vol_output_dir}")
    
    existing_images = list(vol_output_dir.glob("*.png"))
    should_extract = True
    
    if existing_images:
        try:
            from PIL import Image
            with Image.open(existing_images[0]) as img:
                width, height = img.size
                if width > 1200:
                    print(f"  Detected upscaled images (width {width}). Re-extracting at default resolution...")
                    should_extract = True
                else:
                    print(f"  Found {len(existing_images)} existing images with acceptable resolution. Skipping.")
                    should_extract = False
        except Exception as e:
            print(f"  Error checking image size: {e}. Re-extracting...")
            should_extract = True
            
    if should_extract:
        print("  Extracting images (default resolution)...")
        prefix = "page"
        
        cmd_image = [
            "pdftoppm",
            "-png",
            str(pdf_path),
            str(vol_output_dir / prefix)
        ]
        
        try:
            subprocess.run(cmd_image, check=True)
        except subprocess.CalledProcessError as e:
            print(f"  Error running pdftoppm: {e}")
            return

        images = list(vol_output_dir.glob(f"{prefix}-*.png"))
        print(f"  Extracted {len(images)} images.")
        
        for img_path in images:
            filename = img_path.name
            try:
                num_part = filename.replace(f"{prefix}-", "").replace(".png", "")
                page_num = int(num_part)
                new_filename = f"{page_num:04d}.png"
                new_path = vol_output_dir / new_filename
                shutil.move(img_path, new_path)
            except ValueError:
                print(f"  Warning: Could not parse page number from {filename}")

    images = list(vol_output_dir.glob("*.png"))
    page_count = len(images)
    
    existing_texts = list(vol_output_dir.glob("*.txt"))
    if len(existing_texts) == page_count:
        print("  Text files already exist. Skipping text extraction.")
    else:
        print("  Extracting text...")
        for i in range(1, page_count + 1):
            text_filename = f"{i:04d}.txt"
            text_path = vol_output_dir / text_filename
            
            if not text_path.exists():
                cmd_text = [
                    "pdftotext",
                    "-f", str(i),
                    "-l", str(i),
                    str(pdf_path),
                    str(text_path)
                ]
                subprocess.run(cmd_text, check=False)
            
            if i % 50 == 0:
                print(f"    Processed text for page {i}/{page_count}", end='\r')
                
        print(f"    Finished text extraction for Volume {vol_key}.        ")

def generate_manifest():
    print("Generating volume manifests...")
    
    for vol_key in VOLUMES.keys():
        vol_dir = EXTRACTED_DIR / f"volume_{vol_key}"
        if not vol_dir.exists():
            continue
            
        pages = []
        images = sorted(list(vol_dir.glob("*.png")))
        
        for img_path in images:
            filename = img_path.name
            page_num_str = filename.replace(".png", "")
            try:
                page_num = int(page_num_str)
                txt_filename = f"{page_num_str}.txt"
                
                # Store just filenames, relative to the manifest location (volume dir)
                rel_img = filename
                rel_txt = txt_filename
                
                pages.append({
                    "page_num": page_num,
                    "image": rel_img,
                    "text": rel_txt
                })
            except ValueError:
                continue
        
        # Per-volume manifest structure
        manifest = {
            "volume": vol_key,
            "path": ".", # relative to itself
            "pages": pages
        }
        
        manifest_path = vol_dir / "pages.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"Manifest saved to {manifest_path}")

def extract_toc_from_pdf(pdf_path):
    cmd = [
        "pdftohtml",
        "-xml",
        "-stdout",
        "-i",       # ignore images
        "-l", "1",  # process only first page (sufficient for outline)
        str(pdf_path)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running pdftohtml on {pdf_path}: {e}")
        return None

def parse_outline_recursive(outline_element):
    entries = []
    last_entry = None
    
    for child in outline_element:
        if child.tag == "item":
            entry = {
                "title": child.text.strip() if child.text else "",
                "page": int(child.get("page", 0)),
                "children": []
            }
            entries.append(entry)
            last_entry = entry
        elif child.tag == "outline":
            if last_entry is not None:
                last_entry["children"] = parse_outline_recursive(child)
            else:
                pass
                
    return entries

def parse_outline_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print(f"XML Parse Error: {e}")
        return []

    top_outline = root.find("outline")
    if top_outline is None:
        return []
    
    return parse_outline_recursive(top_outline)

def run_toc_extraction():
    full_toc = {}
    
    for vol_key, rel_path in VOLUMES.items():
        pdf_path = PDF_BASE_DIR / rel_path
        if not pdf_path.exists():
            print(f"Warning: PDF not found: {pdf_path}")
            continue
            
        print(f"Extracting TOC for Volume {vol_key}...")
        xml_content = extract_toc_from_pdf(pdf_path)
        
        
        if xml_content:
            toc = parse_outline_xml(xml_content)
            
            # Save volume-specific toc.json
            vol_output_dir = EXTRACTED_DIR / f"volume_{vol_key}"
            ensure_dir(vol_output_dir)
            toc_output_path = vol_output_dir / "toc.json"
            with open(toc_output_path, 'w') as f:
                json.dump(toc, f, indent=2)
            full_toc[f"volume_{vol_key}"] = toc # Keep for consistency with original behavior if needed elsewhere
            print(f"  Found {len(toc)} top-level items.")
        else:
            print("  Failed to extract TOC.")

    # The full_toc is not explicitly saved to a single file anymore, 
    # but can be returned or used as needed by other parts of the pipeline.
    # No global TOC_PATH to write to.

def run_extraction():
    ensure_dir(EXTRACTED_DIR)
    
    for vol_key, path in VOLUMES.items():
        extract_volume(vol_key, path)
        
    generate_manifest()
    run_toc_extraction()

