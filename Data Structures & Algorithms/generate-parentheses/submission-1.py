class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        parenthesis = []
        
        def backtrack(opened, closed):
            if len(parenthesis) == n * 2:
                output.append(''.join(parenthesis))
                return
            
            if opened < n:
                parenthesis.append('(')
                backtrack(opened + 1, closed)
                parenthesis.pop()

            if opened > closed:
                parenthesis.append(')')
                backtrack(opened, closed + 1)
                parenthesis.pop()

        backtrack(0, 0)

        return output