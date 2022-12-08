# Leaf-Similar Trees

"""
    Recursive solution
    Traverse the tree using pre-order traversal with an empty array to store the leave nodes in left to right order,
    for leave node - when node.left and node.right both is None this indicates that we have reached to leave node 
    of the that tree then add leave node to the array and do this for both trees after that 
    return Ture if both tree's array are same otherwise False. 
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def leafSimilar(root1, root2):
    def helper(node, ans):
        if node is not None:
            if node.left is None and node.right is None:
                ans.append(node.val)
            helper(node.left, ans)
            helper(node.right, ans)
        return ans

    ans1 = []
    helper(root1, ans1)
    ans2 = []
    helper(root2, ans2)
    return ans1 == ans2



