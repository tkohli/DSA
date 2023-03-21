#  Number of Zero-Filled Subarrays
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        subarrays of only 0s: e.g., 0,0,0,0
        the # of subarrays ending at 1st 0 is 1: 0,x,x,x
        the # of subarrays ending at 2nd 0 is 2: x,0,x,x, 0,0,x,x
        the # of subarrays ending at 3rd 0 is 3: x,x,0,x, x,0,0,x, 0,0,0,x
        the # of subarrays ending at 4th 0 is 4: x,x,x,0, x,x,0,0, x,0,0,0, 0,0,0,0
        """
        ans, count = 0, 0
        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            ans += count
        return ans


        # ans = 0
        # i=0
        # j=0
        # while j <len(nums):
        #     while j <len(nums) and nums[j]==0:
        #         j+=1
        #     n = j-i
        #     ans += n*(n+1)//2
        #     i=j+1
        #     j+=1
        # return (ans)