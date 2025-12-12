import os
import shutil
from pathlib import Path
from geometor.elements.ingest.config import RESOURCES_DIR
from geometor.elements.ingest.utils import int_to_roman

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def run_image_organization():
    """
    Organizes images from resources/images into a new folder with canonical names.
    """
    images_dir = RESOURCES_DIR / "images"
    output_dir = RESOURCES_DIR / "canonical_images"

    ensure_dir(output_dir)
    print(f"Ensured directory: {output_dir}")

    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg"):
            parts = filename.split('.')
            
            if len(parts) < 4 or parts[0] != 'elem':
                print(f"Skipping non-standard file: {filename}")
                continue

            book = int(parts[1])
            element_type = parts[2]
            element_number = parts[3]
            
            roman_book = int_to_roman(book)
            
            variant = ""
            if len(parts) > 4 and parts[4] != 'jpg':
                variant = f"-{parts[4]}"

            if element_type == "prop":
                new_name = f"{roman_book}.{element_number}{variant}.jpg"
            else:
                new_name = f"{roman_book}.{element_type}.{element_number}{variant}.jpg"

            src_path = images_dir / filename
            dest_path = output_dir / new_name
            
            shutil.copy(src_path, dest_path)
            print(f"Copied and renamed {src_path} to {dest_path}")
