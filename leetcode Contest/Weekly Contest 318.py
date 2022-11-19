# Apply Operations to an Array
from typing import Counter


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums


# Maximum Sum of Distinct Subarrays With Length K
"""
Main issue TLE :(
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # from collections import Counter (elements and their respective count are stored as a dictionary)
        cnt = Counter(nums[:k])
        total = sum(nums[:k])

        res = 0
        if len(cnt) == k:
            res = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            cnt[nums[i]] += 1
            cnt[nums[i-k]] -= 1

            if cnt[nums[i-k]] == 0:
                del cnt[nums[i-k]]

            if len(cnt) == k:
                res = max(res, total)

        return res


# Total Cost to Hire K Workers
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        i, j = candidates, len(costs)-candidates-1
        if len(costs) <= 2 * candidates:
            heap = [(x, 0) for x in costs]
        else:
            heap = [(x, 0) for x in costs[:candidates]] + [(x, 1)
                                                           for x in costs[len(costs)-candidates:]]
        heapq.heapify(heap)

        for _ in range(k):
            cost, direction = heapq.heappop(heap)
            total += cost
            if i <= j:
                if direction:
                    heapq.heappush(heap, (costs[j], 1))
                    j -= 1
                else:
                    heapq.heappush(heap, (costs[i], 0))
                    i += 1

        return total
# https://leetcode.com/problems/minimum-total-distance-traveled/
