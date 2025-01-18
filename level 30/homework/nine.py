def find_python_position(sentence):
    """
    Finds the position of the first occurrence of the word 'Python' in a sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        int: The starting index of the first occurrence of 'Python', or -1 if not found.
    """
    position = sentence.find("Python")
    return position

# Example usage:
sentence = "I am learning Python programming."
position = find_python_position(sentence)

if position != -1:
    print(f"The word 'Python' is found at position: {position}")
else:
    print("The word 'Python' is not found in the sentence.")
