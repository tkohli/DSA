class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        restricted = set(restricted)
        dct = DefaultDict(list)
        for r, n in edges:
            if r in restricted or n in restricted:
                continue
            dct[r].append(n)
            dct[n].append(r)
        ans = 0
        visited = set()
        visited.add(0)
        queue = dct[0]
        while queue:
            node = queue.pop(0)
            visited.add(node)
            for neighbor in dct[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return (len(visited))
