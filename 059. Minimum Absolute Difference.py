# Minimum Absolute Difference
"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
"""


def minimumAbsDifference(self, arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    arr.sort()
    out = [[arr[0], arr[1]]]
    min = arr[0]-arr[1]
    for i in range(1, len(arr)-1):
        if arr[i]-arr[i+1] == min:
            out.append([arr[i], arr[i+1]])
        if arr[i]-arr[i+1] > min:
            min = arr[i]-arr[i+1]
            out = []
            out.append([arr[i], arr[i+1]])
    return (out)
