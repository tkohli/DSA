# User function Template for python3

from typing import List


class Solution:
    def solve(self, N: int, a: int, x: List[int]) -> int:
        first, sec = 0, 0
        for num in X:
            t = abs(num-a)
            if t > first:
                sec = first
                first = t
            elif t > sec:
                sec = t
        return first+sec

        # code here

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N, A = [int(i) for i in input().split()]

        X = [int(i) for i in input().split()]

        obj = Solution()
        res = obj.solve(N, A, X)

        print(res)
# } Driver Code Ends
