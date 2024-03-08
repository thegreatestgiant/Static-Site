import re

from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        divided = node.text.split(delimiter)
        if len(divided) % 2 == 0:
            raise Exception("Invalid Markdown Syntax (missing a delimiter)")
        for i in range(len(divided)):
            str = divided[i]
            if len(str) == 0:
                continue
            if i % 2 == 0:
                nodes.append(TextNode(str, "text"))
            else:
                nodes.append(TextNode(str, text_type))
    return nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        first, i = True, 0
        arr = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        for str in arr:
            if len(str) == 0:
                continue
            if any(str in subl for subl in images):
                if not first:
                    first = True
                    continue
                if i >= len(images):
                    continue
                nodes.append(TextNode(images[i][0], "image", images[i][1]))
                i += 1
                first = False
            else:
                nodes.append(TextNode(str, "text"))
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        first, i = True, 0
        arr = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
        for str in arr:
            if len(str) == 0:
                continue
            if any(str in subl for subl in links):
                if not first:
                    first = True
                    continue
                if i >= len(links):
                    continue
                nodes.append(TextNode(links[i][0], "link", links[i][1]))
                i += 1
                first = False
            else:
                nodes.append(TextNode(str, "text"))
    return nodes


def text_to_textnode(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    return nodes
