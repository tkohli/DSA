"""
If it is possible to allocate x candies to children then it is possible to allocate x-1
candies to children,
There exists a number X such that it is possible to give candies to all y<=x and 
impossible for y>x,
Now we have to use binary search 
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        if sum(candies) == k:
            return 1
        l = 1
        r = sum(candies)//k
        while l < r:
            mid = (l+r)//2
            if sum(i//mid for i in candies) >= k:
                l = mid
            else:
                r = mid-1
        return l
