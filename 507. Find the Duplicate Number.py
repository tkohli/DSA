"""
We have done this question using in-place hashing and 
now let's try to solve this using cycle detection  
"""
nums = [1, 3, 4, 2, 2]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #         for num in nums:
        #             if nums[abs(num)-1]<0:
        #                 return abs(num)
        #             nums[abs(num)-1] *= -1
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
