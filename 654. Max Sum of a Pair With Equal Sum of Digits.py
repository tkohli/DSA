class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct = {}
        ans = -1
        for num in nums:
            tmp = 0
            for ch in str(num):
                tmp += int(ch)
            if tmp not in dct:
                dct[tmp] = num
            else:
                ans = max(ans, dct[tmp]+num)
                dct[tmp] = max(dct[tmp], num)
        return ans
