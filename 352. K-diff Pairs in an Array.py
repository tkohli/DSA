class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dct = {}
        count = 0
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        if k:
            for key in dct.keys():
                if key+k in dct:
                    count += 1
        else:  # k==0
            for val in dct.values():
                if val > 1:
                    count += 1
        return count
