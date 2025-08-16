import os

def modify_uppercase(content):
    return content.upper()

def modify_lowercase(content):
    return content.lower()

def modify_reverse(content):
    return content[::-1]

def modify_word_count(content):
    word_count = len(content.split())
    return f"Word count: {word_count}\n\n{content}"

def modify_add_line_numbers(content):
    lines = content.splitlines()
    numbered = [f"{i+1}: {line}" for i, line in enumerate(lines)]
    return "\n".join(numbered)

def get_modification_choice():
    print("Choose a modification:")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Reverse text")
    print("4. Add word count at top")
    print("5. Add line numbers")
    print("6. Multiple modifications (comma separated, e.g. 1,5)")
    choice = input("Enter option number(s): ")
    return choice

def apply_modifications(content, choices):
    # Map option number to function
    mods = {
        '1': modify_uppercase,
        '2': modify_lowercase,
        '3': modify_reverse,
        '4': modify_word_count,
        '5': modify_add_line_numbers
    }
    result = content
    for c in choices:
        func = mods.get(c)
        if func:
            result = func(result)
    return result

def main():
    filename = input("Enter the filename to read: ")
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        return

    choice = get_modification_choice().replace(" ", "")
    choices = choice.split(",")
    result = apply_modifications(content, choices)

    base, ext = os.path.splitext(filename)
    new_filename = f"modified_{base}{ext}"

    try:
        with open(new_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(result)
        print(f"Modified content written to '{new_filename}'.")
    except Exception as e:
        print(f"Error writing to '{new_filename}': {e}")

if __name__ == "__main__":
    main()