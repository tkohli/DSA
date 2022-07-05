"""
We start by creating a dct and then storing next greatest number in nums2
then we loop through nums1 and append ans else append -1
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = {}
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[i] < nums2[j]:
                    dct[nums2[i]] = nums2[j]
                    break
        ans = []
        for num in nums1:
            if num not in dct:
                ans.append(-1)
            else:
                ans.append(dct[num])
        return ans
