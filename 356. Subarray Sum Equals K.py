from curses import curs_set


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curSum = 0, 0
        dct = {}
        for num in nums:
            curSum += num
            if curSum == k:
                count += 1
            if curSum-k in dct:
                count += dct[curSum]
            if curSum in dct:
                dct[curSum] += 1
            if curSum not in dct:
                dct[curSum] = 1
