def word_frequency(text):
    """Count how many times each word appears in the text."""
    counts = {}
    for word in text.lower().split():
        counts[word] += 1
    return counts


sentence = "the cat and the hat"
print(word_frequency(sentence))
# expected: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
