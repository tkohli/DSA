import heapq
nums = [5, 19, 8, 1]
"""
well I started by sorting the array and then finding bigger val then 
divide it by 2 until i get the totalSum  = oldSum/2.
BUT here come TLE.
So we will use maxHeap which sort of not exists in python so we just 
so -ve all val and then cal value
"""


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        print(heap)
        ans = 0
        k = 0
        while s - k > s / 2:
            x = heapq.heappop(heap)*-1
            k += x/2
            heapq.heappush(heap, -x/2)
            ans += 1
        return ans
