def find_char_index(string, char):
    try:
        index = string.index(char)
        return index
    except ValueError:
        return f"The character '{char}' was not found in the string."

# Example usage
string = "Hello, world!"
char = "w"
print(find_char_index(string, char))
