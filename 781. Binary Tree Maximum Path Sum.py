# Binary Tree Maximum Path Sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum,maxRunningSum =  self.maxSumHelper(root) # branch, triangle
        return maxRunningSum
        
    def maxSumHelper(self,root):
        if root is None:
            return 0,float('-inf')
        leftMaxSumBranch,leftMaxSum = self.maxSumHelper(root.left) 
        rightMaxSumBranch,rightMaxSum = self.maxSumHelper(root.right) 
        maxChildSumBranch = max(leftMaxSumBranch,rightMaxSumBranch)
        val = root.val 
        maxSumBranch = max(maxChildSumBranch+val,val)
        maxSumTriangle = max(maxSumBranch, leftMaxSumBranch+rightMaxSumBranch+val)
        maxRunningSum = max(maxSumTriangle,leftMaxSum,rightMaxSum)
        return maxSumBranch,maxRunningSum
