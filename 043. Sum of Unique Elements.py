# Sum of Unique Elements
"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
"""


def sumOfUnique(nums):
    """
       :type nums: List[int]
       :rtype: int
       """
    sum = 0
    for num in nums:
        if nums.count(num) == 1:
            sum += num
    return sum

   # freq = {}
   # sum = 0
   # for item in nums:
   #     if (item in freq):
   #         freq[item] += 1
   #     else:
   #         freq[item] = 1
   # for x, y in freq.items():
   #     if y == 1:
   #         sum += x
   #     print(x, y)
   # return  (sum)
