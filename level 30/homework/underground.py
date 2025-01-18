def count_word_occurrences(text, word):
    word_count = text.lower().split().count(word.lower())
    return word_count

# Example usage
text = "The quick brown fox jumps over the lazy dog. The fox is quick."
word = "fox"
print(f"The word '{word}' appears {count_word_occurrences(text, word)} times.")
