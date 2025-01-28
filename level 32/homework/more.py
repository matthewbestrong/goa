def sentence_to_words(sentence):
    """
    Splits a sentence into a list of words.

    Parameters:
    sentence (str): The sentence to split.

    Returns:
    list: A list containing the words in the sentence.
    """
    # Use the split() method to divide the sentence into words
    words = sentence.split()
    return words

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog."
word_list = sentence_to_words(sentence)
print(word_list)
