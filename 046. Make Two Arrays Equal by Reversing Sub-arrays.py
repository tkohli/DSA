# Make Two Arrays Equal by Reversing Sub-arrays
"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [1,12], arr = [12,1]
Output: true
"""


def canBeEqual(target, arr):
    """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
    target.sort()
    arr.sort()
    if arr == target:
        return True
    return False
	#--------------------
	dict1 = {}
        dict2 = {}
        for a in arr:
            if a in dict1:
                dict1[a] += 1
            else:
                dict1[a] = 1
        for tar in target:
            if tar in dict2:
                dict2[tar] += 1
            else:
                dict2[tar] = 1
        if dict1 == dict2:
            return True
        return False
