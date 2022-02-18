class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        nums = list(nums)
        stack = []
        for num in nums:
            while stack and stack[-1] > num and k:
                stack.pop()
                k -= 1
            stack.append(num)
        while(k):
            stack.pop()
            k -= 1
        if len(stack) == 0:
            return '0'
        while stack[0] == '0':
            stack.pop(0)  # or we can also take care of this using idx
            if len(stack) == 0:
                return '0'
        if len(stack):
            return "".join(stack)
        return '0'
