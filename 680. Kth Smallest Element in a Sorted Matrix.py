from heapq import heapify, heappop, heappush


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
"""
naive solution will be to convert this to a sorted array 
then find kth element 

Heap we can do is make a heap then goto its left and right 
then pop k elements to get our ans
https://assets.leetcode.com/users/images/dc1a846a-126c-49cb-b9fa-e7a529d86182_1614142241.31893.png

Binary search - some modifications 
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([i for row in matrix for i in row])[k-1]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]  # storing min heap with index
        heapify(heap)
        visited = {(0, 0)}
        for i in range(k-1):
            _, r0, c0 = heappop(heap)
            for r, c in [(r0+1, c0), (r0, c0+1)]:
                if r < n and c < n and (r, c) not in visited:
                    heappush(heap, (matrix[r][c], r, c))
                    visited.add((r, c))
        return heappop(heap)[0]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int):
        """
        There are total K numbers in matrix that are less than Kth number

        Also realize that the count of elements less than ith element is a monotonic property for a sorted array and sorted matrix

        As monotonicity is found we can use Binary Search

        Min value Kth element can have is when K = 0 or low = matrix[0][0]

        Max value Kth element can have is when K = n * n or low = matrix[n-1][n-1]

        Now we will run a binary search and for each mid (m) value we will find it's count, which got easy as matrix is sorted

        Understand that m can be element which is not present in matrix but it will not affect our logic
        """
        # Time Complexity: O(Nlog(max-min) * log(max-min))
        # Space Complexity: O(1)
        n = len(matrix)
        minVal, maxVal = matrix[0][0], matrix[-1][-1]

        def matrixCount(num):
            count = 0
            r, c = 0, n-1
            while r < n and c >= 0:
                if matrix[r][c] <= num:
                    count += c+1
                    r += 1
                else:
                    c -= 1
            return count

        while minVal < maxVal:
            mid = (minVal+maxVal)//2
            count = matrixCount(mid)
            if count < k:
                minVal = mid+1
            else:
                maxVal = mid

        return maxVal
