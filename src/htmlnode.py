class HTMLNode:

    def __init__(self, tag=None, value=None, child=None, props=None):
        self.tag = tag
        self.value = value
        self.children = child
        self.props = props

    def to_html(self):
        raise NotImplementedError("We didn't do this yet")

    def props_to_html(self):
        str = ""
        if self.props is None:
            return str
        for key in self.props:
            str += f' {key}="{self.props[key]}"'
        return str

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, properties={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Input a value please")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, property={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, child, props=None):
        super().__init__(tag, None, child, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("You need to enter a value")
        if self.children is None:
            raise ValueError("Where are your children?")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
