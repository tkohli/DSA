"""
The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
when counting (()(())), our stack will look like this:

[0, 0] after parsing (
[0, 0, 0] after (
[0, 1] after )
[0, 1, 0] after (
[0, 1, 0, 0] after (
[0, 1, 1] after )
[0, 3] after )
[6] after )

We already know that it is balanced so we can solve this 
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        ans = 0
        for b in s:
            if b == '(':
                stack.append(0)
            else:
                tmp = stack.pop()
                stack[-1] += max(2*tmp, 1)
        return stack[0]
