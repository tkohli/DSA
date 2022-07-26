"""
We have to find this using binary search because we are 
given time complexity as log n
So we will first find value then find leftmost ans rightmost value
"""
nums = [5, 7, 7, 8, 8, 10]
target = 8


def searchRange(nums, target):
    if len(nums) < 1:
        return [-1, -1]
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            break
        elif nums[m] < target:
            l = m+1
        else:
            r = m-1
    # check if value is in our nums
    if nums[m] != target:
        return [-1, -1]
    # now checking for rightmost value
    tmp = m
    while l <= tmp:
        mid = (l+tmp)//2
        if nums[mid] == target:
            tmp = mid-1
        else:
            l = mid+1
    tmp = m
    while tmp <= r:
        mid = (r+tmp)//2
        if nums[mid] == target:
            tmp = mid+1
        else:
            r = mid-1
    return ([l, r])


searchRange(nums, target)
