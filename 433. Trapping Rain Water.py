"""
To start with naive solution go to bloack and the use while loop to extend from 
it and check how much water can be stored

Optimizing it we can us 2 array
[0,1,0,2,1,0,1,3,2,1,2,1]
[0,0,1,1,2,2,2,2,3,3,3,3] left max
[3,3,3,3,3,3,3,2,2,2,1,0] right max
[0,0,1,0,1,2,1,0,0,1,0,0] ans => 6 unit of water 
and then further optimize it by using one array 
"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap(self, height) -> int:
        leftMax = [0 for i in range(len(height))]
        rightMax = [0 for i in range(len(height))]
        water = 0
        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1],height[i-1])
        for i in reversed(range(len(height)-1)):
            rightMax[i] = max(rightMax[i+1],height[i+1])
        for i in range(len(height)):
            temp = min(leftMax[i],rightMax[i])
            water+=max(0, (temp-height[i]))
        return water

# trying to optimize it
"""
Two pointer and keep track of max val on left and right
Easy only if we track properly
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        left = 0
        right = len(height)-1
        leftMax, rightMax = 0,0
        while left<right:
            if height[left]<height[right]:
                if leftMax<=height[left]:
                    leftMax = height[left]
                else:
                    ans+=(leftMax-height[left])
                left+=1
            else:
                if rightMax<=height[right]:
                    rightMax = height[right]
                else:
                    ans+=(rightMax-height[right])   
                right-=1
        return ans