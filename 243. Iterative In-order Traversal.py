def iterativeInOrderTraversal(tree, callback):
    """
    InOrder Traversal = LNR
    The main idea should be how to come back 
    i.e. after going left how to go right
    Keep track of prev and current
    Then do callback  
    """
    currentNode = tree
    prevNode = None
    while currentNode is not None:
        if prevNode is None and prevNode == currentNode.parent:
            if currentNode.left is not None:
                currentNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif prevNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode = currentNode.parent
            prevNode = currentNode
            currentNode = nextNode
