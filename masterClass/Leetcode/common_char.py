
def commonChars(words):
    if len(words) < 2:
        return words
    res = []
    print(res)
    word1 = set(words[0])
    print(word1)
    for char in word1:
        frequency = min(word.count(char) for word in words)
        print(frequency)
        res += [char] * frequency
        print(res)
    return res

words = ["bella","label","roller"]
print(commonChars(words))