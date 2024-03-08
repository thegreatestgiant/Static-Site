def markdown_to_blocks(markdown):
    arr, blocks = markdown.split("\n\n"), []
    for block in arr:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks
