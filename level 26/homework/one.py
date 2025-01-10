def reverse_string(s):
    """
    This function takes a string as input and returns the reversed string.
    """
    return s[::-1]

# Example usage
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")
