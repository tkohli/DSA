class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        In this question we are given a directed graph, so we start by 
        finding out distance of each node from our both of sources i.e. 
        node1 and node2

        then we goto our distances array and in that we keep the track of 
        overall min value. 
        """
        m1 = [-1] * len(edges)
        m2 = [-1] * len(edges)
        # populate m1 and m2
        def dfs(node, dist, memo):
            # when node is never reached
            while node != -1 and memo[node] == -1: 
                memo[node] = dist
                dist += 1
                # move to the next node
                node = edges[node] 
        
        dfs(node1, 0, m1)
        dfs(node2, 0, m2)

        minDist = float('inf')
        res = -1   # common node
        for i in range(len(edges)):
            # if node1 and node2 can both reach i
            if m1[i] != -1 and m2[i] != -1:
                if max(m1[i], m2[i]) < minDist:
                    minDist =  max(m1[i], m2[i]) # we are storing overall min value
                    res = i
        return res

        # 1 : [-1,0,1,2]
        # 0 : [0,-1,1,2]
