def isAnagram(s: str, t: str):

        if len(s) != len(t): return False
        s_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in s_dict:
                s_dict[t[i]] -= 1
            else:
                s_dict[t[i]] = -1

        for count in s_dict.values():
            if count != 0:
                return False
        return True
    
# Example usage
print(isAnagram('anagram', 'nagaram'))  # Should print True