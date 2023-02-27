# Floor in BST
"""
Find the greatest value that is which is smaller or equal to X

            10
    5               15
2       6

x = 7 => ans = 6
x = 14 => ans = 10

Do a search in bst such that we maximize our value while ans<=X

Steps:
1. take ans = -1
2. while root
3. if same value return val
4. if x is bigger than cur value that means we can go more right and update our ans
5. else goto left 
"""
def floorInBST(root, X):
    ans = -1
    while root:
        if root.data == X:
            return X
        if X>root.data:
            ans = root.data
            root = root.right
        else:
            root = root.left  

    return ans