class Solution:
    def calculate(self, s: str) -> int:
        if s == "":
            return 0

        result = 0
        sign = 1
        num = 0

        stack = [sign]
        """
        97 + 23
        """
        for ch in s:
            if '0' <= ch and ch <= '9':
                num = num*10 + int(ch)
            elif ch == '+' or ch == '-':
                result += sign * num
                sign = stack[-1] * (1 if ch == "+" else -1)
                num = 0
            elif ch == '(':
                stack.push(sign)

            elif ch == ')':
                stack.pop()

        result += sign * num
        return result
