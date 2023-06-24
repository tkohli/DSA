class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [-1] * n

        stack = []
        for i in range(2 * n, -1, -1):
            curIdx = i % n
            while stack:
                if nums[curIdx] < stack[-1]:
                    ans[curIdx] = stack[-1]
                    break
                else:
                    stack.pop()
            stack.append(nums[curIdx])
        return ans
