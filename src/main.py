import os
import shutil
import sys
from copystatic import copy_files_recursive
from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
dir_path_template = "./template.html"

def main():
    # Accept basepath from CLI, default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print(f"Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print(f"Generating all pages recursively with basepath '{basepath}'...")
    generate_pages_recursive(dir_path_content, dir_path_template, dir_path_docs, basepath)

if __name__ == "__main__":
    main()
