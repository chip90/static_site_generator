import os
import shutil

from copystatic import copy_files_recursive
from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_template = "./template.html"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating all pages recursively...")
    generate_pages_recursive(dir_path_content, dir_path_template, dir_path_public)


main()
