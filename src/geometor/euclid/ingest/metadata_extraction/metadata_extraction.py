import json
import glob
import os
import yaml
from pathlib import Path
from geometor.elements.ingest.config import RESOURCES_DIR, PROJECT_ROOT, METADATA_PATH

def run_metadata_extraction():
    """
    Extracts metadata from book-level article.md files and saves it to a JSON file.
    The content of these files is used to create an intro.rst file.
    """
    metadata = {}
    grav_md_dir = RESOURCES_DIR / 'grav_md'
    files = list(grav_md_dir.glob('*/article.md'))

    files.sort()

    intro_content = ""

    for file_path in files:
        with open(file_path, 'r') as f:
            content = f.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) > 2:
                    try:
                        front_matter = yaml.safe_load(parts[1])
                        key = str(file_path.relative_to(grav_md_dir))
                        metadata[key] = front_matter
                        
                        intro_content += f'.. _{front_matter.get("title", key)}:\n\n'
                        intro_content += f'{front_matter.get("title", key)}\n'
                        intro_content += "=" * len(front_matter.get('title', key)) + "\n"
                        if front_matter.get('subtitle'):
                            intro_content += f'{front_matter.get("subtitle")}\n'
                            intro_content += "-" * len(front_matter.get('subtitle')) + "\n"
                        intro_content += parts[2].strip().replace('===', '')
                        intro_content += "\n\n"

                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML in {file_path}: {e}")

    with open(METADATA_PATH, 'w') as f:
        json.dump(metadata, f, indent=2)

    intro_rst_path = PROJECT_ROOT / 'docsrc' / 'intro.rst'
    with open(intro_rst_path, 'w') as f:
        f.write(".. _intro:\n\n")
        f.write("Introduction\n")
        f.write("============\n\n")
        f.write(intro_content)
