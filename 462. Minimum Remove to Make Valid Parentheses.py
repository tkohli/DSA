class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, ch in enumerate(s):
            if len(stack) > 0 and ch == ')' and stack[-1][0] == '(':
                stack.pop()

            elif ch == '(' or ch == ')':
                stack.append([ch, i])
        ans = ""
        if stack == []:
            return s
        j = 0
        for i, ch in enumerate(s):
            if j < len(stack) and i == stack[j][1]:
                j += 1
                continue
            ans += ch
        return ans
