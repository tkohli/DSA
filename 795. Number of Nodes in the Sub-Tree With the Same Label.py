class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        1. Subtree
        2. Counter 
        3. label
        """
        seen = set()
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0]*n

        def dfs(node):
            cnt = Counter()
            cnt[labels[node]] += 1
            seen.add(node)
            for child in graph[node]:
                if child not in seen:
                    cnt += dfs(child)
            ans[node] = cnt[labels[node]]
            return cnt

        dfs(0)

        return ans
