def shortest_distance(words_dict, word1, word2):
    index_word1 = None
    index_word2 = None
    min_distance = float('inf')

    for i, word in enumerate(words_dict):
        if word == word1:
            index_word1 = i
        if word == word2:
            index_word2 = i
        if index_word1 is not None and index_word2 is not None:
            min_distance = min(min_distance, abs(index_word1 - index_word2))

    return min_distance

# Example usage
words_dict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(shortest_distance(words_dict, word1, word2))  # Output should be 3
