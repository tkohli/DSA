class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, length = 0, 0, 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                length = max(length, 2*right)
            elif right >= left:
                left = right = 0

        left = right = 0

        for ch in s[::-1]:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                length = max(length, 2*right)
            elif right <= left:
                left = right = 0
        return length

        # stack = [-1]
        # ans = 0
        # for i, ch in enumerate(s):
        #     if ch == "(":
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #         else:
        #             ans = max(ans, i-stack[-1])
        # return ans
