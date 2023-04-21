# Maximum Width of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
EXPLANATION
0. Pretty sure we have todo bfs, we can use 2 Queus or deque(doubly ended queue)

1.  According to Problem , we have also to count null nodes b/w two nodes.
		
	     Tree        No of nodes
		  5				1
	     / \
	    3   6			2
	   /   /
	  2   4				2

2.  Above example we have max 2 nodes in a level, but if you see the second level you
will find that right child of 3 is NULL and therefore we also have to count that 
NULL node, and with that the last level now contain 3 nodes, refer to diagram below.

	      5				1
	   /     \
	   3      6				2
	 /  \    /
	2  NULL  4				3 (NULL node also counted)

So Last Level Contains 3 Nodes Including NULL.

3 . We will also assign index to every node
	(if we are startting index from 0)
	
	(below is just formula to find index of node of complete binary tree)
	left(idx) = 2 idx + 1			// left child
	right(idx) = 2 idx + 2			// right child

	At starting root, idx = 0 so left node idx would be 2*0 +1 and right node index would be 2*0 + 2
	Index tree would be

		   0				1
	   /     \
	  1       2				2
	 /  \    /
	3    4  5				3 

	maxWidth would be 5-3+1 = 3

Spoilers : Use a 2D queue


we will also insert index with node , so that we will know,
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = deque([(root, 0)])
        max_width = 0

        while level:
            _, left = level[0]
            _, right = level[-1]
            max_width = max(max_width, right - left + 1)

           

            for i in range(len(level)):
                node, pos = level.popleft()
                if node.left:
                    level.append((node.left, pos * 2))
                if node.right:
                    level.append((node.right, pos * 2 + 1))

        return max_width