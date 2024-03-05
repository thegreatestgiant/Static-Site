from textnode import TextNode


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
