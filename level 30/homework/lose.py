def find_char_index(string):
    char = input("Enter the character to find its index: ")
    if char in string:
        index = string.index(char)
        print(f"The character '{char}' is found at index {index}.")
    else:
        print(f"The character '{char}' was not found in the string.")

# Example usage
string = "Hello, world!"
find_char_index(string)
