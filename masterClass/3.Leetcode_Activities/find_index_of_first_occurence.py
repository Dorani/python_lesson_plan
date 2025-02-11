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

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # Output: 0

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))  # Output: -1
