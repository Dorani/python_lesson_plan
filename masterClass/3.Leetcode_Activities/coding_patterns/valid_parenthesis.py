def valid_parenth(s):
    stack = []
    
    pairs = {
        ')': '(',
        ']': '[',
        '{': '}'
    }
    
    for char in s:
        if char in '([{':
            stack.append[char]
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
            
    return len(stack) == 0