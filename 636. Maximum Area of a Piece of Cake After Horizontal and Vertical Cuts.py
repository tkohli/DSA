h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
"""
So we want to find the max area of cut so definatly we want to 
maximize the height and width of cuts
So we start by sorting it and then finding the 
"""
class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        def getMaxGap(nums, max_size):
            maxGap = max(nums[0], max_size - nums[-1])
            for i in range(1, len(nums)):
                maxGap = max(maxGap, nums[i] - nums[i - 1])
            return maxGap
        return getMaxGap(sorted(H), h) * getMaxGap(sorted(V), w) % 1000000007
#         horizontalCuts.sort()
#         verticalCuts.sort()
#         maxHeight = max(horizontalCuts[0],h-horizontalCuts[-1])
#         for i in range(1,len(horizontalCuts)):
#             maxHeight = max(maxHeight,horizontalCuts[i]-horizontalCuts[i-1])

#         maxwidth = max(verticalCuts[0],w-verticalCuts[-1])
#         for i in range(1,len(verticalCuts)):
#             maxwidth = max(maxwidth,verticalCuts[i]-verticalCuts[i-1])

#         return maxHeight*maxwidth % (10**9+7)