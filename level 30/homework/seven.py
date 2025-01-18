def capitalize_first_letter_in_list(strings):
    """
    Capitalizes the first letter of each string in a given list of strings.
    
    Args:
        strings (list): A list of lowercase strings.
    
    Returns:
        list: A new list with each string's first letter capitalized.
    """
    return [string.capitalize() for string in strings]

# Example usage:
strings_list = ["apple", "banana", "cherry", "date"]
capitalized_list = capitalize_first_letter_in_list(strings_list)
print("Capitalized list:", capitalized_list)
