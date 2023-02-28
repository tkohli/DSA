
def cielInBST(root, X):
    ans = -1
    while root:
        if root.data == X:
            return X
        if X<root.data:
            ans = root.data
            root = root.left
        else:
            root = root.right  

    return ans