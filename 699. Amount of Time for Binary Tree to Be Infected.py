# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TLE solution :)
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        found = None

        def inOrder(pa, node):
            nonlocal found
            if node:
                if not found and node.val == start:
                    print("jkbsd", node)
                    found = node
                parent[node] = pa
                inOrder(node, node.left)
                inOrder(node, node.right)
        inOrder(None, root)
        print(found)
        queue = deque()
        queue.append(found)
        ans = 0
        seen = {found}
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if parent[node] is not None and parent[node] not in seen:
                    queue.append(parent[node])
                    seen.add(parent[node])
                if node.left and node.left not in seen:
                    queue.append(node.left)
                    seen.add(node.left)

                if node.right and node.right not in seen:
                    queue.append(node.right)
                    seen.add(node.right)
            ans += 1

        return ans-1
#         # print(parent[root.left.right])


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def build_graph(parent, node):
            if not node:
                return

            if parent:
                graph[parent.val].append(node)
                graph[node.val].append(parent)

            build_graph(node, node.left)
            build_graph(node, node.right)

        build_graph(None, root)

        vis = set()
        max_infection = 0
        queue = deque([(start, 0)])
        vis.add(start)

        while queue:
            node_val, time = queue.popleft()
            max_infection = max(max_infection, time)

            for nei in graph[node_val]:
                if nei.val not in vis:
                    vis.add(nei.val)
                    queue.append((nei.val, time + 1))

        return max_infection
