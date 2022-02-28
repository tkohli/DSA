class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0  # starting
        j = 0  # ending
        while j < len(nums) and i < len(nums):
            if j < len(nums)-1 and nums[j+1]-nums[j] == 1:
                j += 1
            else:
                if i == j:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(nums[i])+'->'+str(nums[j]))
                i = j+1
                j = i

        return (ans)
