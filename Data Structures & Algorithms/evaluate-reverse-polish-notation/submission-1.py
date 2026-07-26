class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            print(i)
            if i in ('+','-','*','/'):
                print(stack)
                if i == '+':
                    a, b = stack.pop(), stack.pop()
                    operation = a + b
                    stack.append(operation)
                elif i == '-':
                    a, b = stack.pop(), stack.pop()
                    operation = b - a
                    stack.append(operation)
                elif i == '*':
                    a, b = stack.pop(), stack.pop()
                    operation = a * b
                    stack.append(operation)
                elif i == '/':
                    a, b = stack.pop(), stack.pop()
                    operation = int(b / a)
                    stack.append(operation)
            else:
                stack.append(int(i))
        print(stack)
        return stack.pop()