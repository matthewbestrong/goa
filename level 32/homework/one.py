def reverse_and_format(input_string):
    """
    This function takes a string, reverses it,
    and returns a formatted sentence with the reversed string.
    """
    # Reverse the input string using slicing
    reversed_string = input_string[::-1]
    
    # Format the reversed string into a sentence
    result = f"The reverse of '{input_string}' is '{reversed_string}'."
    
    return result

# Example usage:
user_input = input("Enter a string: ")
formatted_message = reverse_and_format(user_input)
print(formatted_message)
