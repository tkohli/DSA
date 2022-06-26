class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        We can have 2 possiblities so lets try to manage it 
        side by side
        """
        cnt = 0
        for i in range(1,len(nums)):
            # check for non increasing
            if nums[i-1]>nums[i]:
                cnt+=1
                if cnt>1:
                    return False
                if i<2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] =nums[i-1]
        return cnt<=1
