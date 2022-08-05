class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        seen = set()
        for element in range(len(edges)):
            count = 0
            currNode = element
            cycleMap = dict()
            while currNode not in seen and currNode != -1:
                count += 1
                seen.add(currNode)
                cycleMap[currNode] = count
                currNode = edges[currNode]
            # gets the max distance
            res = max(res, count + 1 - cycleMap.get(currNode, float("inf")))
        return res
