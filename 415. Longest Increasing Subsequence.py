class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [1 for _ in nums]
        for i, num in enumerate(nums):
            maxSeq = seq[i]
            # find prev max seq and then update it
            for idx in reversed(range(i)):
                if nums[idx] < nums[i]:
                    seq[i] = max(seq[i], seq[idx]+1)
        return max(seq)
