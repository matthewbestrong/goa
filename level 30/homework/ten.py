def find_substring_index(string, substring):
    index = string.find(substring)
    if index != -1:
        print(f"The substring '{substring}' starts at index {index}.")
    else:
        print(f"The substring '{substring}' was not found.")

# Example usage
string = "Hello, this is a test string."
substring = "test"
find_substring_index(string, substring)
