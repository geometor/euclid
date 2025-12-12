import json
import re

def load_json(path):
    if not path.exists():
        return None
    with open(path, 'r') as f:
        return json.load(f)

def sanitize_title(title):
    # 1. Replace multiple spaces
    title = re.sub(r'\s+', ' ', title).strip()
    
    # 2. Fix spaced out words like "C O N T E N T S"
    # Heuristic: if a sequence of single uppercase letters separated by spaces exists, join them.
    # E.g. "B O O K I" -> "BOOK I"
    # Logic: Find patterns of (Char Space)+ Char
    def replacer(match):
        return match.group(0).replace(" ", "")

    title = re.sub(r'\b([A-Z])\s+(?=[A-Z]\b)', r'\1', title)
    
    # 3. Remove trailing periods
    title = title.rstrip('.')
    
    # 4. Convert to snake_case-ish slug
    # Remove punctuation like apostrophes
    title = title.replace("'", "")
    # Replace non-alphanumeric with _
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', title)
    # Lowercase
    slug = slug.lower()
    # Strip underscores
    slug = slug.strip('_')
    
    return slug

def int_to_roman(n):
    """Converts an integer to a Roman numeral."""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "I", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num
