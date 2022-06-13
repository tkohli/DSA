from collections import defaultdict
from threading import local


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        The part where we have to use DFS and disjoint set I thing is enough 
        to make this question hard.
        Note for self: I need to learn about disjoint set as it is very actively used 
        in both contest and some tougher questions

        idea -> with the given pair of indices, we can make a group of 
        indices which are connected, then for each group we can sort 
        their respective strings and then return res.
        """
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        col = []
        seen = set()

        def groupMaking(point):
            nonlocal local
            if point in seen:
                return
            local.append(point)
            seen.add(point)
            for p in graph[point]:
                groupMaking(p)

        for k in graph.keys():
            if k not in seen:
                local = []
                groupMaking(k)
                col.append(local)

        res = list(s)
        for group in col:
            tmp = ''
            for ind in group:
                tmp += s[ind]
            tmp = sorted(tmp)
            group.sort()
            i = 0
            for ind in group:
                res[ind] = tmp[i]
                i += 1

        return "".join(res)
