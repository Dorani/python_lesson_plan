# Problem #8 — Find the Most Common Character

# Given a string s, return the character that appears most frequently.

# If there is a tie, return the character that appears first in the original string.

# Examples
# Input:  s = "banana"
# Output: "a"


def most_common(s):
    lookup = {}
    
    for char in s:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
    
    most_common = s[0]
    most_common_count = lookup[s[0]]
    
    for char in s:
        if lookup[char] > most_common_count:
            most_common = char
            most_common_count = lookup[char]
            
    return most_common


s = "banana"

print(most_common(s))