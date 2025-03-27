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


def find_break_index(line, max_length):
    """
    Finds the rightmost dot in the entire line that is not within a string literal
    and occurs before max_length.
    Returns the index of that dot if found, or -1 if not.
    """
    positions = []
    in_single = False
    in_double = False
    escape = False
    for i, c in enumerate(line):
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if c == "'" and not in_double:
            in_single = not in_single
        elif c == '"' and not in_single:
            in_double = not in_double
        if not in_single and not in_double and c == '.':
            positions.append(i)
    valid_positions = [pos for pos in positions if pos < max_length]
    if valid_positions:
        return max(valid_positions)
    return -1


def break_long_line(line, max_length=79):
    """
    Breaks a long line into multiple lines if it exceeds max_length.
    The break is attempted at the rightmost dot ('.') outside of string literals that is before max_length.
    The first part ends with the dot; the remainder is placed on a new line indented with the original indent + 4.
    Recursively applies until the entire line is within max_length.
    """
    if len(line) <= max_length:
        return [line]

    match = re.match(r'^(\s*)', line)
    indent = match.group(1) if match else ""

    break_index = find_break_index(line, max_length)
    if break_index == -1:
        break_index = max_length - 1

    first_part = line[:break_index + 1].rstrip()
    remainder = line[break_index + 1:].lstrip()

    new_indent = indent + "    "
    remainder_line = new_indent + remainder
    broken_remainder = break_long_line(remainder_line, max_length)
    return [first_part] + broken_remainder


def insert_empty_line_after_function(lines):
    """
    Inserts an empty line after the end of a function block.

    Heuristic:
      - When a line starts with 'def ' (after leading whitespace), record its indent.
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
                        if new_lines and new_lines[-1].strip() != "":
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

    lines = reindent_lines(lines)
    code = "\n".join(lines)

    operator_pattern = r'\s*((>>=|<<=|\*\*=|//=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|:=|==|!=|>=|<=|\*\*|//|<<|>>|[+\-*/%=><&|^~]))\s*'
    code = re.sub(operator_pattern, r' \1 ', code)
    code = re.sub(r',(\S)', r', \1', code)

    lines = code.splitlines()
    lines = collapse_inner_spaces(lines)

    final_lines = []
    for line in lines:
        if len(line) > 79:
            broken = break_long_line(line, 79)
            final_lines.extend(broken)
        else:
            final_lines.append(line)

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
      - If an IndentationError is detected, prompting the user to attempt to fix it using fix_indent_syntax().
      - Otherwise, calling format_code() to process the content.
      - Writing the formatted code back to the file.
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
        print("Formatting applied successfully.")
    except Exception as e:
        print("Error writing file:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
