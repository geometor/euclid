
import os
import re

def find_refs_in_enunciation(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    book_match = re.search(r'elem\.(\d+)\.\d+\.xml', file_path)
    if not book_match:
        return None, None
    book_num = int(book_match.group(1))

    if book_num == 1:
        enunc_match = re.search(r'<div4 type="Enunc".*?>(.*?)</div4>', content, re.DOTALL)
        if enunc_match:
            if '<ref' in enunc_match.group(1):
                return file_path, enunc_match.group(1)
    elif 2 <= book_num <= 6:
        head_split = re.split(r'<head>.*?</head>', content, 1)
        if len(head_split) > 1:
            after_head = head_split[1]
            p_tags = re.findall(r'<p>(.*?)</p>', after_head, re.DOTALL)
            if p_tags and '<ref' in p_tags[0]:
                return file_path, p_tags[0]
    return None, None

def main():
    base_dir = 'resources/xml/books'
    problem_files = []

    for i in range(1, 7):  # Books 1 to 6
        book_dir = os.path.join(base_dir, f'{i:02d}.xml')
        file_path = book_dir
        
        # Read the entire book file
        with open(file_path, 'r') as f:
            book_content = f.read()

        # Split the book content into individual propositions
        # Assuming each proposition is within <div3 id="elem.X.Y" ...> ... </div3>
        propositions = re.findall(r'(<div3 id="elem\.(\d+)\.(\d+)"[^>]*>.*?</div3>)', book_content, re.DOTALL)

        for prop_content, book_num_str, prop_num_str in propositions:
            prop_id = f"elem.{book_num_str}.{prop_num_str}"
            
            if int(book_num_str) == 1:
                enunc_match = re.search(r'<div4 type="Enunc"[^>]*>(.*?)</div4>', prop_content, re.DOTALL)
                if enunc_match and '<ref' in enunc_match.group(1):
                    problem_files.append((prop_id, enunc_match.group(1).strip()))
            elif 2 <= int(book_num_str) <= 6:
                head_split = re.split(r'<head>.*?</head>', prop_content, 1)
                if len(head_split) > 1:
                    after_head = head_split[1]
                    p_tags = re.findall(r'<p>(.*?)</p>', after_head, re.DOTALL)
                    if p_tags and '<ref' in p_tags[0]:
                        problem_files.append((prop_id, p_tags[0].strip()))

    if problem_files:
        print("Files with <ref> tags in enunciation:")
        for file_id, enunciation_content in problem_files:
            print(f"- {file_id}: {enunciation_content}")
    else:
        print("No files found with <ref> tags in enunciation for Books 1-6.")

if __name__ == "__main__":
    main()
