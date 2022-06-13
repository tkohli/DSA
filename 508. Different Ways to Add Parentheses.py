"""
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
So we can do this using recursion then we do get ans based on expression 
"""


expression = "1+2-1"


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(n, op, m):
            n = int(n)
            m = int(m)
            if op == '+':
                return (n+m)
            if op == '-':
                return (n-m)
            if op == '*':
                return (n*m)

        def helper(l, r):
            ans = []
            for i in range(l, r):
                if expression[i] in '+-*/':
                    ans += [calc(le, expression[i], ri) for le in helper(l, i)
                            for ri in helper(i+1, r)]
            return ans if len(ans) != 0 else [int(expression[l:r])]

        return helper(0, len(expression))
