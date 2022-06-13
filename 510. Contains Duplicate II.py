class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        for i, num in enumerate(nums):
            if num not in dct:
                dct[num] = i
                continue
            if i-dct[num] <= k:
                return True
            dct[num] = i

        return False
