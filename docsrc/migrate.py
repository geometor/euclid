import frontmatter
from pathlib import Path
from m2r import convert
import shutil
import os
from bs4 import BeautifulSoup

def under(s, char='='):
    return char * len(s)

def get_slug(post, md_file):
    if 'slug' in post and post.get('slug'):
        return post['slug']
    return md_file.stem

def get_title(post):
    title = post.get('subtitle') or post.get('title')
    if not title:
        return "" # handle cases with no title
    return title

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove the lemma div
    for div in soup.find_all('div', {'id': 'elem.13.13.l.1', 'class': 'lemma'}):
        div.decompose()

    # Remove divs that are sometimes wrapped around the content
    for div in soup.find_all('div'):
        div.unwrap()

    # Unwrap nested <a> tags
    for a in soup.find_all('a'):
        if a.find('a'):
            a.unwrap()

    # Remove pb tags
    for pb in soup.find_all('pb'):
        pb.decompose()

    return str(soup)

def migrate():
    source_root = Path('.archive/elements')
    dest_root = Path('docsrc/elements2')

    if dest_root.exists():
        shutil.rmtree(dest_root)
    dest_root.mkdir()

    img_dest_dir = dest_root / 'images'
    img_dest_dir.mkdir(exist_ok=True)

    for md_file in source_root.glob('**/*.md'):
        book_dir_part = None
        for part in md_file.parts:
            if '.book-' in part:
                book_dir_part = part
                break

        if not book_dir_part:
            continue

        try:
            post = frontmatter.load(md_file)
        except TypeError as e:
            if "multiple values for argument 'content'" in str(e):
                with md_file.open(encoding='utf-8') as f:
                    metadata, content = frontmatter.parse(f.read())
                if 'content' in metadata:
                    del metadata['content']
                post = frontmatter.Post(content, **metadata)
            else:
                raise e

        book_num = book_dir_part.split('.')[0]
        dest_dir = dest_root / book_num
        dest_dir.mkdir(exist_ok=True)

        slug = get_slug(post, md_file)
        rst_file_path = dest_dir / (slug + '.rst')

        with rst_file_path.open(mode='w') as rst_file:
            title = get_title(post)
            if not title:
                print(f"Warning: No title found for {md_file}. Using filename as title.")
                title = md_file.stem

            rst_file.write(title + '\n')
            rst_file.write(under(title) + '\n\n')

            if 'taxonomy' in post and post.get('taxonomy') and 'category' in post.get('taxonomy'):
                category_list = post['taxonomy']['category']
                if category_list is not None:
                    categories = [cat for cat in category_list if cat is not None]
                    if categories:
                        categories_str = ', '.join(categories)
                        rst_file.write(f'.. index:: {categories_str}\n\n')

            image_name = md_file.stem + '.png'
            image_path = Path('.archive/images') / image_name
            if image_path.exists():
                shutil.copy(image_path, img_dest_dir / image_name)
                rst_file.write(f'.. image:: ../images/{image_name}\n')
                rst_file.write('   :align: right\n')
                rst_file.write('   :width: 300px\n\n')

            cleaned_content = clean_html(post.content)
            # Remove the '===' from the content *before* conversion
            cleaned_content = cleaned_content.replace('===', '')
            rst_content = convert(cleaned_content)
            rst_file.write(rst_content)

if __name__ == '__main__':
    migrate()
    print("Migration complete.")
