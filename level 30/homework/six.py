def capitalize_first_letter(sentence):
    """
    Capitalizes the first letter of the given sentence.
    
    Args:
        sentence (str): The sentence to modify.
    
    Returns:
        str: The sentence with the first letter capitalized.
    """
    return sentence.capitalize()

# Example usage:
user_input = input("Enter a sentence: ")
capitalized_sentence = capitalize_first_letter(user_input)
print("Capitalized sentence:", capitalized_sentence)
