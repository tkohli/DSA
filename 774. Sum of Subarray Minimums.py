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


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        ans = 0
        
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]]>= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                ans += (count * arr[mid])

            stack.append(i)
        
        return ans % MOD
