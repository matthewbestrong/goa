def insert_word_at_index(sentence, word, index):
    """
    Inserts a word into the sentence at the specified character index.

    Parameters:
    sentence (str): The original sentence.
    word (str): The word to insert.
    index (int): The character index at which to insert the word.

    Returns:
    str: The modified sentence with the word inserted.
    """
    if index < 0 or index > len(sentence):
        raise ValueError("Index is out of the valid range.")

    # Insert the word at the specified index
    modified_sentence = sentence[:index] + word + sentence[index:]

    return modified_sentence

# Example usage:
original_sentence = "The quick brown fox."
word_to_insert = " agile"
insertion_index = 10

new_sentence = insert_word_at_index(original_sentence, word_to_insert, insertion_index)
print(new_sentence)
