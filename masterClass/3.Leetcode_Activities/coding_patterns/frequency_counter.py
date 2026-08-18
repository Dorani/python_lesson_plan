#1. Frequency Map
#Problem

#Given a list of words, return the frequency of each word.

#words = ["ai", "ml", "ai", "rag", "ml", "ai"]

def frequency(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count