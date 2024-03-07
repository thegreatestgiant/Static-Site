from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type is not "text":
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
        images = extract_markdown_images(node.text)
        for image_tup in images:
            one = node.text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(one[0]) is not 0:
                nodes.append(TextNode(one[0], "text"))
            nodes.append(TextNode(image_tup[0], "image", image_tup[1]))
            if len(one) > 0 and len(one[1]) is not 0 and not (r"!\[(.*?)\]\((.*?)\)") in one[1]:
                nodes.append(TextNode(one[1], "text"))
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        for link_tup in links:
            one = node.text.split(f"![{link_tup[0]}]({link_tup[1]})", 1)
            if len(one[0]) is not 0:
                nodes.append(TextNode(one[0], "text"))
            nodes.append(TextNode(link_tup[0], "link", link_tup[1]))
            if len(one[1]) is not 0 and not (r"!\[(.*?)\]\((.*?)\)") in one[1]:
                nodes.append(TextNode(one[1], "text"))
    return nodes
