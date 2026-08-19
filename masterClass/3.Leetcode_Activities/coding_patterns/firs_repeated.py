# Problem #5 — Find the First Repeated Character

# Given a string s, return the first character that appears more than once.

# If no character repeats, return -1.

# Examples
# Input:  s = "abcdca"
# Output: "c"


def first_repeated(s):
    lookup = {}
    
    for letter in s:
        if letter in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1

        if lookup[letter] > 1:
            return letter
    return -1


s = "abcdca"
print(first_repeated(s))