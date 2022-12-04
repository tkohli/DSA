class Solution:
  def minimumAverageDistance(self, nums: List[int]) -> int:
    # o(n) time and O(1) space
    """
    Naive Solution would be to use slicing and then find average 
    Optimization keeping prefix sum, then more optimise it by keeping just running sum. 
    """
    n = len(nums)
    ans = -1 # store index
    minAvgDiff = float("inf") # overall min avg diff
    curPrefixSum = 0
    total = sum(nums)
    
    for i in range(n):
      curPrefixSum += nums[i]
      leftSum = curPrefixSum//(i+1)
        if i!=n-1:
          rightSum = (total - curPrefixSum)//(n-i-1)
        else:
          rightSum = (total - curPrefixSum)
        curDiff = abs(leftSum-rightSum)
        if curDiff<minAvgDiff:
          minAvgDiff = curDiff
          ans = i
    return ans
    
