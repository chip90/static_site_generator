class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # LeafNode doesn't accept children parameter as it doesn't have children
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        # All leaf nodes must have a value
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        # If there is no tag, return the value as raw text
        if self.tag is None:
            return self.value
        
        # Otherwise, render as an HTML tag with props
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # ParentNode requires tag and children, doesn't accept value parameter
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        # ParentNode must have a tag
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        # ParentNode must have children
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        # Generate HTML for all children
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        # Return HTML with opening tag, children's HTML, and closing tag
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"