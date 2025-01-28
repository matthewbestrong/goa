

def split_paragraph_into_sentences(paragraph):
    """
    Splits a paragraph into sentences using NLTK's sentence tokenizer.

    Parameters:
    paragraph (str): The paragraph to split.

    Returns:
    list: A list of sentences.
    """
    sentences = (paragraph)
    return sentences

# Example usage:
paragraph = "Dr. Smith graduated from the Univ. of California. He joined Google Inc. in 2020. He said, 'AI is the future.'"
sentences = split_paragraph_into_sentences(paragraph)
for sentence in sentences:
    print(sentence)
