def markdown_to_blocks(markdown):
    arr, blocks = markdown.split("\n\n"), []
    for block in arr:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block: str):
    first = block.split(" ")[0]
    # Heading
    if "#" in first and not len(first) > 6 and all(x == first[0] for x in first):
        return "heading"
    # Code
    if block.startswith("```") and block.endswith("```"):
        return "code"
    firsts = [line.split()[0] for line in block.splitlines()]
    if all(x == firsts[0] for x in firsts):
        if ">" in firsts:
            return "quote"
        if "*" in firsts or "-" in firsts:
            return "unordered_list"
    works = True
    for i in range(len(firsts)):
        if f"{i + 1}" not in firsts[i]:
            works = False
    if works:
        return "ordered_list"
    return "paragraph"

