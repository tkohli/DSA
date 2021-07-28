# Sort Array By Parity
"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""


def sortArrayByParity(nums):
    even = []
    odd = []
    for num in nums:
        if nums % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    opt = even+odd
    return opt
