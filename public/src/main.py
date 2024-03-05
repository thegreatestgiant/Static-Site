from textnode import TextNode


def main():
    node1 = TextNode("This is a text node", "bold", "https://boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://boot.dev")
    print(node1 == node2)
    print(node1)


main()
