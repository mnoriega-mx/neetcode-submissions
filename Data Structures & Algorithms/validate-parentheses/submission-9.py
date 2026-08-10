class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }

        stack = []

        for p in s:
            if stack and p in matches:
                if matches[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        return True