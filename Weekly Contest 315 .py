# Largest Positive Integer That Exists With Its Negative
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = set(nums)
        nums.sort()
        print(nums,n)
        for num in nums:
            if num in n and -num in n:
                return abs(num)
        return -1
    
# Count Number of Distinct Integers After Reverse Operations


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = set(nums)
        for num in nums:
            n.add(int(str(num)[::-1]))
        return len(n)


# Sum of Number and Its Reverse
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for x in range(10**5 + 1):
            if x + int(str(x)[::-1]) == num:
                return True
        return False


# Count Subarrays With Fixed Bounds
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res, left = 0, 0
        pos1, pos2 = -1, -1
        for right in range(n):
            if nums[right] == minK:
                pos1 = right
            if nums[right] == maxK:
                pos2 = right
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
            res += max(0, min(pos1, pos2) - left + 1)

        return res


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastmn = 0
        lastmx = 0
        mn = float("inf")
        mx = -1
        x = 0
        ans = 0
        for i in range(len(nums)):
            if(nums[i] == minK):
                lastmn = i+1
            if(nums[i] == maxK):
                lastmx = i+1
            if(nums[i] < minK or nums[i] > maxK):
                lastmn = 0
                lastmx = 0
                x = i+1
            if(lastmn and lastmx):
                ans += min(lastmn-x, lastmx-x)

        return ans
#         totalSum = 0
#         n = len(nums)
#         for k in range(n+1):`
#             for i in range(n-k+1):
#                 minCurrent = 1e9
#                 maxCurrent = -1

#                 for j in range(i, i+k):
#                     if nums[j] < minCurrent:
#                         minCurrent = nums[j]

#                     if nums[j] > maxCurrent:
#                         maxCurrent = nums[j]
#                 if minCurrent==minK and maxCurrent==maxK:
#                     totalSum += 1

#         return totalSum
