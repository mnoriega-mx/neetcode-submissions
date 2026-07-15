class Solution:
    def isValid(self, s: str) -> bool:

        matches = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack = []
        for i in s:
            if i not in matches:
                stack.append(i)
            elif not stack or matches[i] != stack.pop():
                return False

        if not stack:
            return True
        return False