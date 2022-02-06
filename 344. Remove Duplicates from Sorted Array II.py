from collections import Counter


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        temp = []
        temp2 = []
        num = 0
        count = Counter(nums)
        for idx in range(len(nums)):
            if count[nums[idx]] <= 2:
                temp.append(nums[idx])
                num += 1
            else:
                temp2.append(nums[idx])
                count[nums[idx]] -= 1
        nums[:] = temp[:]+temp2[:]
        return num
