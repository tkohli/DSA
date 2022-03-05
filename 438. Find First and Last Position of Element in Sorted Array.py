"""
[5 7 7 8 8 10]
 0 1 2 3 4  5

8 target start,end => [3,4]

1. First we will implement Binary search to find target
2. From my target expand to left and right
"""
class Solution:
    def searchRange(self, nums, target: int) :
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                # return mid
                break
            if nums[mid]<target:  # 7<8
                left = mid+1
            else:
                right = mid-1
        if nums[mid]!=target:
            return [-1,-1]
        left = mid
        right = mid
        #  5 5 5
        while left-1 >= 0 and nums[left-1]==target: 
            left-=1
        while right+1 < len(nums) and nums[right+1]==target: 
            right+=1

        return [left,right]


"""
Can we somehow try to do this searching in Binary search format
Yes 
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                # return mid
                break
            if nums[mid]<target:  # 7<8
                left = mid+1
            else:
                right = mid-1
        if nums[mid]!=target:
            return [-1,-1]
        temp = mid
        midTemp = mid
        while left<=temp:
            mid = (left+temp)//2
            if nums[mid]==target:
                temp = mid-1
            else:
                left = mid+1
        ans = []
        ans.append(left)
        temp = midTemp
        while temp<=right:
            mid = (right+temp)//2
            if nums[mid]==target:
                temp = mid+1
            else:
                right = mid-1
        ans.append(right)
        return (ans)