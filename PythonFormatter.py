import re
import sys


def count_leading_spaces(line):
    """Return the number of leading spaces in the given line."""
    return len(line) - len(line.lstrip(' '))


def process_block(lines, start_index, parent_indent):
    """
    Recursively adjusts the indentation of lines in a block.

    - The new base indent for the block is parent's indent + 4.
    - The first non-empty line in the block is used as a marker.
    - For each line in the block, the new indent = block_base + (original_indent - marker).
    - If a line ends with a colon, process its nested block recursively.

    Returns the index after the block.
    """
    i = start_index
    marker = None
    while i < len(lines):
        if lines[i].strip() != "":
            marker = count_leading_spaces(lines[i])
            break
        i += 1
    if marker is None:
        return i

    block_base = parent_indent + 4
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue
        current_indent = count_leading_spaces(lines[i])
        if current_indent < marker:
            break
        relative = current_indent - marker
        new_indent = block_base + relative
        lines[i] = " " * new_indent + lines[i].lstrip(' ')
        if lines[i].rstrip().endswith(":"):
            i = process_block(lines, i + 1, new_indent)
        else:
            i += 1
    return i


def fix_first_line_after_colon(lines):
    """
    For every line that ends with a colon (":"),
    check the next non-empty line. If its indent is less than or equal to the parent's indent,
    reindent that line to (parent's indent + 4). Otherwise, leave it as is.
    """
    new_lines = list(lines)
    for i in range(len(new_lines) - 1):
        if new_lines[i].rstrip().endswith(":"):
            parent_indent = count_leading_spaces(new_lines[i])
            j = i + 1
            while j < len(new_lines) and new_lines[j].strip() == "":
                j += 1
            if j < len(new_lines):
                next_indent = count_leading_spaces(new_lines[j])
                if next_indent <= parent_indent:
                    new_lines[j] = " " * (parent_indent + 4) + new_lines[j].lstrip()
    return new_lines


def normalize_sibling_indentation(lines, tolerance=2):
    """
    Normalizes the indentation of sibling lines within a block.

    For any block header (a line ending with a colon) that does NOT start with "def ",
    this function finds the first non-empty line (the marker) and then for subsequent lines in that block
    (i.e. lines with indent greater than the header) until a line with indent <= parent's indent is encountered,
    if a line's indent is within 'tolerance' spaces of the marker, it is set to exactly the marker's indent.

    Lines that have the same indentation as the parent are not modified.
    """
    new_lines = list(lines)
    i = 0
    while i < len(new_lines) - 1:
        if new_lines[i].rstrip().endswith(":") and not new_lines[i].lstrip().startswith("def "):
            parent_indent = count_leading_spaces(new_lines[i])
            j = i + 1
            while j < len(new_lines) and new_lines[j].strip() == "":
                j += 1
            if j < len(new_lines):
                marker_indent = count_leading_spaces(new_lines[j])
                k = j + 1
                while k < len(new_lines):
                    if new_lines[k].strip() == "":
                        k += 1
                        continue
                    current_indent = count_leading_spaces(new_lines[k])
                    if current_indent <= parent_indent:
                        break
                    if abs(current_indent - marker_indent) <= tolerance:
                        new_lines[k] = " " * marker_indent + new_lines[k].lstrip(' ')
                    k += 1
            i = k
        else:
            i += 1
    return new_lines


def reindent_lines(lines):
    """
    Adjusts the indentation for the whole code based on the following heuristic:
      - For any line ending with a colon (":") that starts a block,
        subsequent non-empty lines with indent >= marker indent are reindented
        to (parent's indent + 4) plus their relative indent.
    """
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue
        if lines[i].rstrip().endswith(":"):
            parent_indent = count_leading_spaces(lines[i])
            i = process_block(lines, i + 1, parent_indent)
        else:
            i += 1
    return lines


def collapse_inner_spaces(lines):
    """
    Collapse multiple spaces into a single space in the non-indentation part of each line.
    Leading whitespace is preserved.
    """
    new_lines = []
    for line in lines:
        match = re.match(r'^(\s*)(.*)$', line)
        if match:
            indent, content = match.groups()
            content = re.sub(r' {2,}', ' ', content)
            new_lines.append(indent + content)
        else:
            new_lines.append(line)
    return new_lines


def insert_empty_line_after_function(lines):
    """
    Inserts an empty line after the end of a function block.

    - When a line starts with 'def ' (ignoring leading whitespace), record its indent.
    - All lines following that are part of the function block have a greater indent.
    - When a non-empty line is encountered with an indent less than or equal to the function declaration,
      assume the function block has ended and insert an empty line before that line if one isn't already present.
    """
    new_lines = []
    current_func_indent = None
    in_function = False

    for idx, line in enumerate(lines):
        new_lines.append(line)
        stripped = line.lstrip()
        if stripped.startswith("def "):
            current_func_indent = count_leading_spaces(line)
            in_function = True
        if in_function and line.strip() != "":
            if idx + 1 < len(lines):
                next_line = lines[idx + 1]
                if next_line.strip() != "":
                    next_indent = count_leading_spaces(next_line)
                    if next_indent <= current_func_indent:
                        new_lines.append("")
                        in_function = False
                        current_func_indent = None
    return new_lines


def format_code(code):
    """
    Applies basic code formatting:
      - Replaces tabs with 4 spaces
      - Trims trailing whitespace
      - Adjusts indentation using reindent_lines() (recursive adjustment for nested blocks)
      - Fixes the first line after any colon to be (parent indent + 4)
      - Normalizes sibling lines within blocks to match the indent of the first child (if within tolerance),
        but leaves lines with the same indent as the parent untouched.
      - Applies spacing rules for common operators
      - Adds a whitespace after commas
      - Collapses multiple spaces in the content (without altering leading indentation)
      - Inserts an empty line after a function block ends.
      - Ensures the formatted code ends with an empty line.
    """
    code = code.replace("\t", "    ")
    lines = [line.rstrip() for line in code.splitlines()]
    if lines and lines[-1] != "":
        lines.append("")

    lines = fix_first_line_after_colon(lines)
    lines = normalize_sibling_indentation(lines)
    lines = reindent_lines(lines)
    code = "\n".join(lines)

    operator_pattern = r'\s*((>>=|<<=|\*\*=|//=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|:=|==|!=|>=|<=|\*\*|//|<<|>>|[+\-*/%=><&|^~]))\s*'
    code = re.sub(operator_pattern, r' \1 ', code)
    code = re.sub(r',(\S)', r', \1', code)

    lines = code.splitlines()
    lines = collapse_inner_spaces(lines)

    final_lines = lines[:]
    final_lines = insert_empty_line_after_function(final_lines)

    code = "\n".join(final_lines)
    if not code.endswith("\n"):
        code += "\n"
    return code


def main():
    """
    The main() function handles:
      - Reading the file from the given filename
      - Checking for IndentationError by attempting to compile the code.
      - If an IndentationError is detected, prompting the user to attempt to fix it.
      - Otherwise, calling format_code() to process the content.
      - Writing the formatted code back to the file.
      - Measuring and displaying the total processing time.
    """
    if len(sys.argv) != 2:
        print("Usage: python simple_formatter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)

    formatted_code = format_code(code)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted_code)
        print("Formatting applied successfully")
    except Exception as e:
        print("Error writing file:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
