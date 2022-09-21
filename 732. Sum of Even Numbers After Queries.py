class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # maintain even total S, remove A[index] from S if it is even, then add A[index] + val back
        # Time O(N + Q), Space O(1), N is the length of nums, and Q is the number of queries
        even_total = 0
        for num in nums:
            if num % 2 == 0:
                even_total += num

        res = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                even_total -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even_total += nums[i]
            res.append(even_total)
        return res
