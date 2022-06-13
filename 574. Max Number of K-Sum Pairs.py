class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        tmp = defaultdict(int)
        ans = 0
        for num in nums:
            if num in tmp:
                ans += 1
                tmp[num] -= 1
                if tmp[num] == 0:
                    del tmp[num]

            else:
                tmp[k-num] += 1
        return ans


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l]+nums[r] > k:
                r -= 1
            else:
                l += 1
        return ans
