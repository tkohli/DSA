"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def insert(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]
        if node:
            clone = Node(node.val)
            nodeMap[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(self.insert(neighbor, nodeMap))
            return clone
        return None

    def cloneGraph(self, node):
        nodeMap = {}
        return self.insert(node, nodeMap)


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}
        output = Node(node.val)
        visited[node.val] = [output]
        queue = [output]
        while queue:
            node = queue.pop()
            for neigh in node.neighbors:
                if neigh not in visited:
                    visited[neigh.val] = Node(neigh.val)
                    queue.append(neigh)
                visited[node.val].neighbors.append(visited[neigh].val)
        return output
