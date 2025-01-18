def capitalize_first_letter(string):
    """
    Capitalizes the first letter of the given string.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with its first letter capitalized.
    """
    if not string:
        return "Input string is empty"
    return string[0].upper() + string[1:]

# Example usage:
input_string = "hello world"
capitalized_string = capitalize_first_letter(input_string)
print("Capitalized string:", capitalized_string)
