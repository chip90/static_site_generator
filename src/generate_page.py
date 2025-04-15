import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read markdown
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    # Extract title
    title = extract_title(markdown)
    # Replace placeholders
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    # Ensure directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    # Write output
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)
