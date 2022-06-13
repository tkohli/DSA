directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
"""
Based on intuition I am starting of a stack 
RLRSLL
R + L = 2
S + R = 0
directions = "SsSsLsSLLRSRSSRLRRRRLLRRLSSRR"

"""
ans = 0
stack = [directions[0]]
for d in directions[1:]:
    if d == 'S' and stack[-1] == 'R':
        ans += 1
        stack.append('S')
    elif d == 'L' and stack[-1] == 'R':
        ans += 2
        stack.append('S')
    elif d == 'L' and stack[-1] == 'S':
        ans += 1
        stack.append('S')
    else:
        stack.append(d)
print(ans)

"""
This naive approach fails as we gof or complex tasks
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        left = right = 0
        # in starting avoid all left cars as they will not crash
        for d in directions:
            if d == 'L':
                ans += left
            else:
                # as we get anyother car a left car can now crash
                left = 1
        for d in directions[::-1]:
            if d == 'R':
                ans += right
            else:
                right = 1
        return ans
