# All Paths From Source to Target
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def helper(i, curarr):
            if i == len(graph) - 1:
                ans.append(curarr + [i])
                return
            else:
                for node in graph[i]:
                    helper(node, curarr + [i])
        helper(0, [])
        return ans
