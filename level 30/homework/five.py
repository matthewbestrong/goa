def to_lowercase(mixed_string):
    """
    Converts a mixed-case string to all lowercase letters.
    
    Args:
        mixed_string (str): The string to convert.
    
    Returns:
        str: The string in all lowercase letters.
    """
    return mixed_string.lower()

# Example usage:
input_string = "ThiS Is A MiXed CaSe StrinG"
lowercase_string = to_lowercase(input_string)
print("Original string:", input_string)
print("Lowercase string:", lowercase_string)
