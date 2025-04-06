from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    """
    Convert a TextNode to a LeafNode based on its text_type.
    
    Args:
        text_node: A TextNode object
        
    Returns:
        A LeafNode object
        
    Raises:
        Exception: If the text_node's text_type is not recognized
    """
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected TextNode object")
    
    if text_node.text_type == TextType.NORMAL:
        # TextType.NORMAL: Return a LeafNode with no tag, just a raw text value
        return LeafNode(tag=None, value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        # TextType.BOLD: Return a LeafNode with a "b" tag and the text
        return LeafNode(tag="b", value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        # TextType.ITALIC: "i" tag, text
        return LeafNode(tag="i", value=text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        # TextType.CODE: "code" tag, text
        return LeafNode(tag="code", value=text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        # TextType.LINK: "a" tag, anchor text, and "href" prop
        if text_node.url is None:
            raise ValueError("TextNode with LINK type must have a url")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props
        if text_node.url is None:
            raise ValueError("TextNode with IMAGE type must have a url")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception(f"Invalid TextType: {text_node.text_type}")
