class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        dct = defaultdict(list)
        for a,b in roads:
            dct[a].append(b)
            dct[b].append(a)
        print(dct)
        ans = 0
        def dfs(node,parent):
            nonlocal ans
            people = 0
            for neigh in dct[node]:
                if neigh == parent:
                    continue
                p = dfs(neigh,node) 
                people += p
                ans += int(ceil(p/seats))
            return people +1


        dfs(0,-1)
        return ans