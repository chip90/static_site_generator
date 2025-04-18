import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, dest_entry_path)
        elif os.path.isfile(entry_path) and entry.endswith(".md"):
            # Replace .md with .html for output
            dest_html = dest_entry_path[:-3] + ".html" if dest_entry_path.endswith(".md") else dest_entry_path + ".html"
            generate_page(entry_path, template_path, dest_html)
