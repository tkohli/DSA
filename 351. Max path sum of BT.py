def maxPathSum(tree):
    _, x = maxPathSumHelper(tree)
    return x


def maxPathSumHelper(root):
    if root is None:
        return (0, float("-inf"))
    leftMaxSumBranch, leftMaxSum = maxPathSumHelper(root.left)
    rightMaxSumBranch, rightMaxSum = maxPathSumHelper(root.right)
    maxChildSumBranch = max(leftMaxSumBranch, rightMaxSumBranch)
    val = root.value
    maxSumBranch = max(maxChildSumBranch+val, val)
    maxSumRootNode = max(leftMaxSumBranch+val+rightMaxSumBranch, maxSumBranch)
    maxRunningSum = max(leftMaxSum, rightMaxSum, maxSumRootNode)
    return (maxSumBranch, maxRunningSum)
