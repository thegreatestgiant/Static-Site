from htmlnode import LeafNode


class TextNode:
    def __init__(self, test=None, text_type=None, url=None):
        self.text = test
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(text_node):
        type = text_node.text_type
        if type == "text":
            return LeafNode(None, text_node.text)
        if type == "bold":
            return LeafNode("b", text_node.text)
        if type == "italic":
            return LeafNode("i", text_node.text)
        if type == "code":
            return LeafNode("code", text_node.text)
        if type == "link":
            return LeafNode("a", text_node.text, text_node.url)
        if type == "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")
