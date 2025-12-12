import os
import re
import json
import glob
from pathlib import Path
from geometor.elements.ingest.config import PROPOSITION_INDEX_PATH, EXTRACTED_DIR
from geometor.elements.ingest.utils import load_json

# Regex patterns
PROP_START_RE = re.compile(r"^\s*PROPOSITION\s+([IVXLCDM\d]+)\.?\s*$", re.IGNORECASE)
PROP_END_RE = re.compile(r"(?:being\s+)?what\s+it\s+was\s+required\s+to\s+(?:do|prove)|Q\.?\s*E\.?\s*[DF]\.?", re.IGNORECASE)

def get_book_from_path(path):
    # heuristic to extract book name from path
    parts = path.parts
    for part in parts:
        if part.lower().startswith("book"):
            return part
    return "unknown"

def process_folder(folder_path: Path, volume):
    print(f"Scanning {folder_path}...")
    
    files = sorted(folder_path.glob("*.txt"))
    if not files:
        return []
    
    propositions = []
    current_prop = None
    
    book_name = get_book_from_path(folder_path)

    for file_path in files:
        filename = file_path.name
        try:
            page_num = int(filename.replace(".txt", ""))
        except ValueError:
            continue
            
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
            
        total_lines = len(lines)
            
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if not line_stripped:
                continue
                
            start_match = PROP_START_RE.match(line_stripped)
            
            if not start_match and line_stripped.upper() == "PROPOSITION":
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line:
                        num_match = re.match(r"^([IVXLCDM\d]+)\.?$", next_line, re.IGNORECASE)
                        if num_match:
                            prop_label = num_match.group(1)
                            
                            if current_prop:
                                current_prop["status"] = "incomplete_end"
                                propositions.append(current_prop)
                            
                            current_prop = {
                                "volume": volume,
                                "book": book_name,
                                "label": prop_label,
                                "start_page": page_num,
                                "start_page_total_lines": total_lines,
                                "start_line_index": i, 
                                "start_line_text": line_stripped + " " + next_line,
                                "end_page": None,
                                "end_page_total_lines": None,
                                "end_line_index": None,
                                "end_line_text": None,
                                "status": "open"
                            }
                        break
                continue
            
            if start_match:
                prop_label = start_match.group(1)
                
                if current_prop:
                    current_prop["status"] = "incomplete_end"
                    propositions.append(current_prop)
                
                current_prop = {
                    "volume": volume,
                    "book": book_name,
                    "label": prop_label,
                    "start_page": page_num,
                    "start_page_total_lines": total_lines,
                    "start_line_index": i,
                    "start_line_text": line_stripped,
                    "end_page": None,
                    "end_page_total_lines": None,
                    "end_line_index": None,
                    "end_line_text": None,
                    "status": "open"
                }
                continue
            
            if current_prop:
                if PROP_END_RE.search(line_stripped):
                    current_prop["end_page"] = page_num
                    current_prop["end_page_total_lines"] = total_lines
                    current_prop["end_line_index"] = i
                    current_prop["end_line_text"] = line_stripped
                    current_prop["status"] = "closed"
                    propositions.append(current_prop)
                    current_prop = None
    
    if current_prop:
        current_prop["status"] = "incomplete_end_at_eof"
        propositions.append(current_prop)
        
    return propositions

def run_analysis():
    all_propositions = []
    
    for root, dirs, files in os.walk(EXTRACTED_DIR):
        root_path = Path(root)
        folder_name = root_path.name.lower()
        
        is_prop_folder = "propositions" in folder_name
        is_book_folder = "book" in folder_name
        
        has_txt = any(f.endswith(".txt") for f in files)
        
        if (is_prop_folder or is_book_folder) and has_txt:
            vol = "unknown"
            # Check longest strings first to avoid substring matches (e.g. "volume_i" in "volume_iii")
            if "volume_iii" in str(root_path).lower(): vol = "III"
            elif "volume_ii" in str(root_path).lower(): vol = "II"
            elif "volume_i" in str(root_path).lower(): vol = "I"
            
            props = process_folder(root_path, vol)
            all_propositions.extend(props)
            
    with open(PROPOSITION_INDEX_PATH, 'w') as f:
        json.dump(all_propositions, f, indent=2)
        
    print(f"Saved {len(all_propositions)} propositions to {PROPOSITION_INDEX_PATH}")
