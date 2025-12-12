import json
import os
import shutil
import re
from pathlib import Path
from geometor.elements.ingest.config import EXTRACTED_DIR, VOLUMES, RESOURCES_DIR
from geometor.elements.ingest.utils import load_json, sanitize_title

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def get_max_page(pages):
    if not pages:
        return 0
    return max(p['page_num'] for p in pages)

def assign_ranges(toc_entries, start_page, end_page, parent_path, assignments):
    """
    Recursive function to assign page ranges to paths.
    assignments: dict mapping page_num -> path
    """
    
    sorted_entries = sorted(toc_entries, key=lambda x: x['page'])
    
    current_start = start_page
    
    for i, entry in enumerate(sorted_entries):
        entry_page = entry['page']
        
        if entry_page > current_start:
            for p in range(current_start, entry_page):
                if p < end_page:
                    assignments[p] = parent_path
        
        if i < len(sorted_entries) - 1:
            next_start = sorted_entries[i+1]['page']
        else:
            next_start = end_page
            
        title = entry.get('title', 'untitled')
        slug = sanitize_title(title)
        
        if not slug:
            slug = f"section_{entry_page}"
            
        entry_path = parent_path / slug
        
        children = entry.get('children', [])
        
        if children:
            assign_ranges(children, entry_page, next_start, entry_path, assignments)
        else:
            for p in range(entry_page, next_start):
                if p < end_page:
                    assignments[p] = entry_path
        
        current_start = next_start
        
    if current_start < end_page:
        for p in range(current_start, end_page):
            assignments[p] = parent_path

def run_organization():
    for vol_key in VOLUMES.keys():
        vol_dir = EXTRACTED_DIR / f"volume_{vol_key}"
        vol_manifest_path = vol_dir / "pages.json"
        vol_toc_path = vol_dir / "toc.json"
        
        manifest = load_json(vol_manifest_path)
        vol_toc = load_json(vol_toc_path)
        
        if not manifest or not vol_toc:
            print(f"Skipping {vol_key} (missing manifest or TOC)")
            continue
            
        print(f"Organizing {vol_key}...")
        
        vol_pages = manifest['pages']
        max_page = get_max_page(vol_pages)
        
        # We want paths relative to the volume root
        assignments = {}
        assign_ranges(vol_toc, 1, max_page + 1, Path("."), assignments)
        
        new_pages_list = []
        
        for page_info in vol_pages:
            p_num = page_info['page_num']
            
            # Relative subfolder
            target_subfolder = assignments.get(p_num, Path("unknown"))
            
            # Full path to target directory
            target_dir_full = vol_dir / target_subfolder
            ensure_dir(target_dir_full)
            
            # Source files
            # page_info['image'] is relative to vol_dir (e.g. "0001.png") or possibly deeper if re-run
            # But initially extraction puts them at root of vol_dir.
            # Let's check if the file exists at the location specified in manifest.
            
            current_img_rel = Path(page_info['image'])
            current_txt_rel = Path(page_info['text'])
            
            src_img_full = vol_dir / current_img_rel
            src_txt_full = vol_dir / current_txt_rel
            
            filename_img = src_img_full.name
            filename_txt = src_txt_full.name
            
            dest_img_full = target_dir_full / filename_img
            dest_txt_full = target_dir_full / filename_txt
            
            # Move only if source differs from dest
            if src_img_full != dest_img_full:
                if src_img_full.exists():
                    shutil.move(src_img_full, dest_img_full)
            
            if src_txt_full != dest_txt_full:
                if src_txt_full.exists():
                    shutil.move(src_txt_full, dest_txt_full)
                
            new_entry = page_info.copy()
            
            # Update manifest path to be relative to vol_dir
            # dest_img_full is /.../resources/heath/volume_I/book_i/0001.png
            # We want book_i/0001.png
            
            try:
                rel_path_img = dest_img_full.relative_to(vol_dir)
                rel_path_txt = dest_txt_full.relative_to(vol_dir)
                
                new_entry['image'] = str(rel_path_img)
                new_entry['text'] = str(rel_path_txt)
                new_pages_list.append(new_entry)
            except ValueError:
                print(f"Error calculating relative path for {dest_img_full}")

        manifest['pages'] = new_pages_list
        
        with open(vol_manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"Reorganization complete for {vol_key}. Updated {vol_manifest_path}")