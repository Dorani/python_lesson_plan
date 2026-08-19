# Problem #4 — First Unique Character

# Given a string s, return the index of the first non-repeating character.

# If there isn't one, return -1.

# Examples:

# Input:  s = "leetcode"
# Output: 0


# Input:  s = "loveleetcode"
# Output: 2


# Input:  s = "aabb"
# Output: -1

def first_non_repeating(s):
    lookup = {}
   
    for letter in s:
        if letter in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1

    i = 0    
    for letter in s:
        if lookup[letter] == 1:
            return i
        else:
            i += 1
    return -1


s = "loveleetcode"
print(first_non_repeating(s))