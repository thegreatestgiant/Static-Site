import os
from pathlib import Path
from os.path import isfile
from re import template
import shutil

from block_html import markdown_to_html_node


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path, 0o755)
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f"{from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def extract_title(markdown: str):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            text = line.lstrip("#")
            return text
    raise Exception("All markdown needs a title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path)
    md = f.read()
    f.close()

    temp = open(template_path)
    template = temp.read()
    temp.close()

    node = markdown_to_html_node(md)
    content = node.to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    f = open(dest_path, "w")
    f.write(template)
    f.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_dir = os.path.join(dir_path_content, filename)
        dest_dir = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_dir):
            dest_dir = Path(dest_dir).with_suffix(".html")
            generate_page(from_dir, template_path, dest_dir)
        else:
            generate_pages_recursive(from_dir, template_path, dest_dir)
