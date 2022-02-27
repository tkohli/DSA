class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1
        while (l < r):
            if height[l] <= height[r]:
                tmp = height[l]*(r-l)
                l += 1
            else:
                tmp = height[r]*(r-l)
                r -= 1

            ans = max(ans, tmp)
        return ans
