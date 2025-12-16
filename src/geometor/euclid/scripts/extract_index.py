import re
import glob
import os
from pathlib import Path

# Directories to process
DIRS = [
    "resources/heath/volume_I/english_index",
    "resources/heath/volume_II/englishindex",
    "resources/heath/volume_III/general_index"
]

OUTPUT_DIR = "resources/heath/index"
PEOPLE_FILE = os.path.join(OUTPUT_DIR, "people.yaml")
TOPICS_FILE = os.path.join(OUTPUT_DIR, "topics.yaml")

def clean_line(line):
    # Remove page numbers and volume refs (e.g., "I. 338-9", "1. 148")
    # This is an aggressive regex to kill number sequences
    line = re.sub(r'(I|II|III|1|l)\.\s*[\d\s\.,\-n]+', ' ', line)
    line = re.sub(r'\s\d+[\d\s\.,\-]*', ' ', line)
    
    # Remove special chars often found in OCR noise
    line = re.sub(r'[«»<>]', '', line)
    
    # Remove quotes
    line = line.replace('"', '').replace("'", "")

    # Recombine spaced letters (e.g. "S i d e" -> "Side")
    # Look for patterns of 3+ letters separated by single spaces
    def recombine(match):
        return match.group(0).replace(" ", "")
        
    line = re.sub(r'\b([A-Za-z]\s){2,}[A-Za-z]\b', recombine, line)
    
    return line.strip()

def is_person(term):
    # Heuristics for people
    # 1. "Name, Initials." or "Name, Name"
    if re.match(r'^[A-Z][a-z]+,\s[A-Z].*', term):
        return True
    if re.match(r'^[A-Z][a-z]+,\s[A-Z][a-z]+', term):
        return True
    
    # 2. "Name (Initials)"
    if re.match(r'^[A-Z][a-z]+\s\([A-Z]\.\)', term):
        return True
        
    # 3. Known historical figures (single names)
    singles = [
        "Euclid", "Plato", "Aristotle", "Archimedes", "Apollonius", 
        "Theaetetus", "Eudoxus", "Pythagoras", "Thales", "Proclus",
        "Pappus", "Heron", "Geminus", "Ptolemy", "Simplicius",
        "Porphyry", "Zeno", "Zenodorus", "Xenocrates"
    ]
    if term in singles:
        return True
        
    # 4. "al-..." names
    if "al-" in term:
        return True
        
    # 5. Names with " b. " (ibn)
    if " b. " in term:
        return True

    return False

import difflib
from collections import Counter

# ... (imports remain)

# ... (clean_line, is_person remain)

def merge_similar_terms(term_counts, threshold=0.85):
    # Bucket by first character to speed up
    buckets = {}
    for term in term_counts:
        key = term[0].lower() if term else ""
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(term)
        
    merged = {}
    total_skipped = set()
    
    for key in buckets:
        terms = buckets[key]
        # Sort by frequency desc, then length
        sorted_terms = sorted(terms, key=lambda x: (-term_counts[x], len(x)))
        
        skipped = set()
        for i, term1 in enumerate(sorted_terms):
            if term1 in skipped:
                continue
            
            merged[term1] = term_counts[term1]
            
            for j in range(i + 1, len(sorted_terms)):
                term2 = sorted_terms[j]
                if term2 in skipped:
                    continue
                    
                ratio = difflib.SequenceMatcher(None, term1.lower(), term2.lower()).ratio()
                if ratio >= threshold:
                    merged[term1] += term_counts[term2]
                    skipped.add(term2)
        
        total_skipped.update(skipped)
                
    return merged

def extract():
    people_counts = Counter()
    topics_counts = Counter()
    
    all_files = []
    root_dir = Path("/home/phi/PROJECTS/geometor/euclid")
    
    for d in DIRS:
        path = root_dir / d
        if not path.exists():
            print(f"Warning: {path} does not exist")
            continue
        all_files.extend(glob.glob(str(path / "*.txt")))
    
    print(f"Processing {len(all_files)} files...")
    
    for fpath in all_files:
        with open(fpath, 'r') as f:
            lines = f.readlines()
            
        # Basic line join (same as before)
        cleaned_lines = []
        buffer = ""
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.endswith("-"):
                buffer += line[:-1]
            else:
                if buffer:
                    line = buffer + line
                    buffer = ""
                cleaned_lines.append(line)
        
        for line in cleaned_lines:
            # Clean text
            clean = clean_line(line)
            if not clean or len(clean) < 3:
                continue
            
            # Simple heuristic: take text up to first colon or specialized delimiter
            term = clean.split(":")[0].strip()
            term = term.split("  ")[0].strip() # double space often separates term from page nums
            
            # cleanup trailing punctuation
            term = term.strip(".,;")
            
            if not term:
                continue

            # Skip single numbers or very short digit-only strings
            if re.match(r'^[\d\s\(\)]*$', term):
                continue
                
            if is_person(term):
                people_counts[term] += 1
            else:
                if len(term) > 2:
                    topics_counts[term] += 1

    print("Deduplicating...")
    final_people = merge_similar_terms(people_counts, threshold=0.9)
    final_topics = merge_similar_terms(topics_counts, threshold=0.85)

    # Sort alphabet
    sorted_people = sorted(final_people.keys())
    sorted_topics = sorted(final_topics.keys())
    
    # Write YAML
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(PEOPLE_FILE, 'w') as f:
        for p in sorted_people:
            f.write(f"- {p}\n")
            
    with open(TOPICS_FILE, 'w') as f:
        for t in sorted_topics:
            f.write(f"- {t}\n")

    print(f"Extracted {len(sorted_people)} people and {len(sorted_topics)} topics.")
    print(f"Saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    extract()
