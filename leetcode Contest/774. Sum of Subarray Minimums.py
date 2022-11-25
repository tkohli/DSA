arr = [3, 1, 2, 4]

# Naive Solution


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            tmp = float("inf")
            for j in range(i, len(arr)):
                tmp = min(tmp, arr[j])
                ans += tmp
        return ans % (10**9+7)
