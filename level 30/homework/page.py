def count_the_occurrences(paragraph):
    word_count = paragraph.lower().split().count('the')
    return word_count

# Example usage
paragraph = "The quick brown fox jumps over the lazy dog. The dog sleeps."
print(f"The word 'the' appears {count_the_occurrences(paragraph)} times.")
