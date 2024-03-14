def markdown_to_blocks(markdown):
    arr, blocks = markdown.split("\n\n"), []
    for block in arr:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block: str):
    first = block.split("", 1)[0]
    # Heading
    if "#" in first and not len(first) > 6 and all(x == block[0] for x in block):
        return "heading"
    # Code
    if block.startswith("```") and block.endswith("```"):
        return "code"
    lines = block.splitlines()
    firsts = []
    for line in lines:
        firsts.append(line.split()[0])
    if all(x == firsts[0] for x in firsts):
        if ">" in firsts:
            return "quote"
        if "*" in firsts or "-" in firsts:
            return "unordered_list"
        works = True
        for i in range(len(firsts)):
            if (i + 1) not in firsts[i]:
                works = False
        if works:
            return "ordered_list"
    return "paragraph"

