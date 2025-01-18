def count_char_occurrences(string):
    char = input("Enter a character to count its occurrences: ")
    count = string.count(char)
    print(f"The character '{char}' appears {count} times in the string.")

# Example usage
string = "hello, how are you doing today?"
count_char_occurrences(string)
