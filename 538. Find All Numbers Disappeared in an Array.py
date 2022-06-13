class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k = set(nums)
        ans = []
        for i in range(1, len(nums)+1):
            if i not in k:
                ans.append(i)

        return ans
