import os
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content_index = "./content/index.md"
dir_path_template = "./template.html"
dir_path_public_index = "./public/index.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating index page...")
    generate_page(dir_path_content_index, dir_path_template, dir_path_public_index)


main()
