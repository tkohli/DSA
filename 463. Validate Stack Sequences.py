"""
With pointer and reversed stack to pop vals
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []
        for push in pushed:
            while stack != [] and stack[-1] == popped[-1]:
                popped.pop()
                stack.pop()
            else:
                stack.append(push)

        return stack == popped


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for push in pushed:
            stack.append(push)
            while stack != [] and stack[-1] == popped[j]:
                j += 1
                stack.pop()

        return j == len(popped)
