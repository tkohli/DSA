class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num1-num2)
                elif token == '*':
                    stack.append(num1*num2)
                elif token == '/':
                    stack.append(int(num1/num2))
            else:
                stack.append(token)
        return stack[-1]
