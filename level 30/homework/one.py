def convert_to_uppercase(strings_list):
    """
    Converts a list of lowercase strings to uppercase.

    Args:
        strings_list (list): List of lowercase strings.
    
    Returns:
        list: List of uppercase strings.
    """
    # Use a list comprehension to convert each string to uppercase
    uppercase_list = [string.upper() for string in strings_list]
    return uppercase_list

# Example usage
lowercase_strings = ["hello", "world", "python", "coding"]
uppercase_strings = convert_to_uppercase(lowercase_strings)
print("Uppercase strings:", uppercase_strings)
