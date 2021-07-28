# Relative Sort Array
"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""


def relativeSortArray(self, arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    lst = []
    for arr in arr2:
        count = arr1.count(arr)
        for _ in range(count):
            lst.append(arr)
            arr1.remove(arr)
    arr1.sort()
    return (lst+arr1)
    # dict = {}
    # lst = []
    # for arr in arr1:
    #     if arr in dict:
    #         dict[arr] += 1
    #     else:
    #         dict[arr] = 1
    # print(dict)
    # for arr in arr2:
    #     if arr in dict:
    #         i = 1
    #         while i <= dict[arr]:
    #             lst.append(arr)
    #             arr1.remove(arr)
    #             i += 1
    #         # print(arr, dict[arr])
    #     # print(arr)
    #     arr1.sort()
    # return (lst+arr1)
