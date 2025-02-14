# Approach:
# Check if the length of the needle is greater than the length of the haystack. If so, return -1 immediately because the needle can't fit in the haystack.
# Loop through the haystack and check substrings of the same length as the needle.
# If a substring matches the needle, return the starting index.
# If no match is found after checking all possible substrings, return -1.

def strStr(haystack: str, needle: str) -> int:
    # If the needle is an empty string, return 0
    if not needle:
        return 0
    
    # If the needle's length is greater than the haystack, return -1
    if len(needle) > len(haystack):
        return -1
    
    # Loop through the haystack and check each substring of the length of needle
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    # If no match found, return -1
    return -1

# Explanation:
# if not needle: return 0 handles the edge case where the needle is an empty string
# (according to some interpretations of the problem).
# The loop runs from 0 to len(haystack) - len(needle) + 1 to avoid checking 
# out-of-bound substrings.

# If a match is found, it returns the starting index i.
# If no match is found after checking all possible substrings, it returns -1.
# Time Complexity:
# The time complexity is O((n - m + 1) * m), where n is the length of the haystack and m is the length of the needle. In the worst case, the algorithm checks all possible substrings of length m in n

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # Output: 0

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))  # Output: -1
