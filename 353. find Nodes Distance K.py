# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    nodeToParent = {}
    populateNodeToParents(tree, nodeToParent)
    targetNode = getNodeFormValue(target, tree, nodeToParent)

    return bfs(targetNode, nodeToParent, k)


def bfs(targetNode, nodeToParent, k):
    seen = {targetNode.value}
    queue = [(targetNode, 0)]
    while queue:
        node, distance = queue.pop(0)
        if distance == k:
            out = [x.value for x, y in queue]
            out.append(node.value)
            return out
        currentNode = [node.left, node.right, nodeToParent[node.value]]
        for node in currentNode:
            if node is not None and node.value not in seen:
                seen.add(node.value)
                queue.append((node, distance+1))
            else:
                continue
        return []


def getNodeFormValue(val, root, nodeToParent):
    if root.value == val:
        return root
    # find its parent and then
    nodeParent = nodeToParent[val]
    if nodeParent.left and nodeParent.left.value == val:
        return nodeParent.left

    return nodeParent.right


def populateNodeToParents(node, nodeToParent, parent=None):
    if node is not None:
        nodeToParent[node.value] = parent
        populateNodeToParents(node.left, nodeToParent, node)
        populateNodeToParents(node.right, nodeToParent, node)
