class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dct = {0: 0}
        cur = 0
        maxLen = 0
        for idx, val in enumerate(nums, 1):
            if val == 0:
                cur -= 1
            else:
                cur += 1
            if cur not in dct:
                dct[cur] = idx
            else:
                maxLen = max(maxLen, idx-dct[cur])
        return maxLen
