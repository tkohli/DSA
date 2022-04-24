class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        tmp = nums[0]
        tmp.sort()
        for i in range(len(nums)):
            nums[i] = set(nums[i])
        for t in tmp:
            for i, num in enumerate(nums):
                if t not in num:
                    break

                if i == len(nums)-1:
                    ans.append(t)

        return ans
