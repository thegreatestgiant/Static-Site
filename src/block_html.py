from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnode
from markdown_blocks import block_to_block_type, markdown_to_blocks
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    items = []
    for block in blocks:
        type = block_to_block_type(block)
        items.append(globals()[f"{type}_to_html"](block))
    div = ParentNode("div", items)
    return div


def inline_children(text):
    text = text.splitlines()
    text = " ".join(text)
    nodes = text_to_textnode(text)
    children = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def paragraph_to_html(block):
    children = inline_children(block)
    return ParentNode("p", children)


def quote_to_html(block):
    lines = block.splitlines()
    for i in range(len(lines)):
        if lines[i].startswith(">"):
            lines[i] = lines[i].lstrip("> ")
    lines = " ".join(lines)
    children = inline_children(lines)
    return ParentNode("blockquote", children)


def code_to_html(block):
    children = inline_children(block)
    code = ParentNode("code", children)
    pre = ParentNode("pre", code)
    return pre


def unordered_list_to_html(block: str):
    lines = block.splitlines()
    items = []
    for line in lines:
        line = line.partition(" ")[2]
        children = inline_children(line)
        item = ParentNode("li", children)
        items.append(item)
    ulist = ParentNode("ul", items)
    return ulist


def ordered_list_to_html(block: str):
    lines = block.splitlines()
    items = []
    for line in lines:
        line = line.partition(" ")[2]
        children = inline_children(line)
        item = ParentNode("li", children)
        items.append(item)
    olist = ParentNode("ol", items)
    return olist


def heading_to_html(block):
    children = inline_children(block)
    num = len(block.split(" ")[0])
    return ParentNode(f"h{num}", children)
