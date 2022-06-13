from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        The cost of connecting two points [xi, yi] and [xj, yj] is the 
        manhattan distance between them: |xi - xj| + |yi - yj|, where 
        |val| denotes the absolute value of val.

        Discussing about the solution we can see that it is a clear graph problem 
        but the question arises that which algorithm to use, since we have to 
        calculate the value as well as so we will not use dijkastra 
        Let's try using Kruskal or prims algo 

        For Kruskal we need to implement union find which don't know 

        Prims Algorithm

        Initialize some variables:

        n - Number of nodes of the graph.
        mstCost - Cost to build the MST.
        edgesUsed - Number of edges included in the MST.
        inMST - Array to track if a node was already included in MST or not.
        heap - A min-heap to pick minimum weight edge, each element of heap is a pair of (edge \space weight, \space node)(edge weight, node).

        Initially, we start with node 00 and the cost to include this node will be 00, thus we push all adjacent edges of node 00 in heapheap with their respective weightsweights using a for-loop. However, to make the code implementation cleaner, we will simply initialize the heapheap with the pair (0, \space 0)(0, 0), which represents a temporary edge to node 00 with a weight of 00.

        We pop elements from the heapheap and attempt to add them to the tree until edgesUsededgesUsed becomes equal to nn. We initially added one temporary edge, thus we stop when nn edges are added in the MST.

        We get the minimum weighted edge and the node from the top of heapheap and pop it.
        If this node is already present in our MST ( inMST[node] == true )(inMST[node]==true) we discard this edge.
        Otherwise, we include this node in our MST, increment edgesUsededgesUsed by 11, add the edge's weight to the mstCostmstCost, and push the edges of this node into the heapheap.
        We return the total cost of MST, mstCostmstCost.
        """

        n = len(points)
        heap = [(0, 0)]
        inMST = [False] * n
        mstCost = 0
        edgesUsed = 0
        while edgesUsed < n:
            weight, currentNode = heappop(heap)
            if inMST[currentNode]:
                continue
            inMST[currentNode] = True
            mstCost += weight
            edgesUsed += 1

            for nextNode in range(n):
                if not inMST[nextNode]:
                    nextWeight = abs(points[currentNode][0]-points[nextNode][0]) + \
                        abs(points[currentNode][1]-points[nextNode][1])
                    heappush(heap, (nextWeight, nextNode))

        return mstCost
