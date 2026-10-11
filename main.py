def simple_rstrip(code):
    """
    Remove trailing whitespace from each line of the given code.
    """
    lines = code.splitlines()
    new_lines = [line.rstrip() for line in lines]
    return '\n'.join(new_lines)

def change_indentation(code):
    """
    Change the 4-space indentation of the given code into 2-space indentation.
    """
    lines = code.splitlines()
    new_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line:
            new_lines.append(' ' * ((len(line) - len(stripped_line))//2) + stripped_line)
        else:
            new_lines.append('')
    return '\n'.join(new_lines)

def delete_empty_lines(code):
    """
    Delete empty lines from the given code.
    """
    lines = code.splitlines()
    new_lines = [line for line in lines if line.strip()]
    return '\n'.join(new_lines)

def delete_comments(code):
    """
    Delete comments from the given code.
    """
    lines = code.splitlines()
    new_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        if "#" in stripped_line:
            comment_index = stripped_line.index("#")
            new_lines.append(line[:comment_index])
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def delete_docstrings(code):
    """
    Delete docstrings from the given code.
    """
    lines = code.splitlines()
    new_lines = []
    in_docstring = False
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            if not in_docstring:
                in_docstring = True
                continue
            else:
                in_docstring = False
                continue
        if not in_docstring:
            new_lines.append(line)
    return '\n'.join(new_lines)

def delete_operators_spaces(code):
    """
    Delete spaces around operators in the given code.
    """
    operators = ["+", "-", "*", ",", "/", "%", "=", "==", "!=", "<", ">", "<=", ">="]
    for operator in operators:
        code = code.replace(f" {operator} ", operator)
        code = code.replace(f"{operator} ", operator)
        code = code.replace(f" {operator}", operator)
    return code


def extrem_compression(code):
    """
    Put a maximum of the code in a single line.
    """
    lines = code.splitlines()
    new_lines = []
    last_indent = 0
    keywords = ["def", "class", "if", "elif", "else", "for", "while", "try", "except", "finally", "with"]
    for i in range(len(lines)):
        new_indent = len(lines[i]) - len(lines[i].lstrip())
        if new_indent == last_indent and not any(lines[i].lstrip().startswith(keyword) for keyword in keywords):
            new_lines.append(";" + lines[i].strip())
        else:
            new_lines.append("\n" + lines[i])
        last_indent = new_indent
    lines = ''.join(new_lines)[1:].splitlines()
    new_lines = []
    last_indents = [0, 0]
    for i in range(len(lines)):
        new_indent = len(lines[i]) - len(lines[i].lstrip())
        if last_indents[0] < last_indents[1] and new_indent < last_indents[1]:
            new_lines[-1] = (new_lines[-1][1:]).lstrip()
        new_lines.append("\n" + lines[i])
        last_indents[0] = last_indents[1]
        last_indents[1] = new_indent
    return ''.join(new_lines)[1:]

if __name__ == "__main__":
    
    INPUT_PATH = "input.py"
    OUTPUT_PATH = "output.py"

    with open(INPUT_PATH, "r") as input_file:
        input_code = input_file.read()

    input_code = change_indentation(input_code)
    input_code = delete_docstrings(input_code)
    input_code = delete_comments(input_code)
    input_code = simple_rstrip(input_code)
    input_code = delete_empty_lines(input_code)
    input_code = delete_operators_spaces(input_code)
    #input_code = extrem_compression(input_code)
    with open(OUTPUT_PATH, "w") as output_file:
        output_file.write(input_code)