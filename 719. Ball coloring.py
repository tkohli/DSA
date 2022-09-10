# https://practice.geeksforgeeks.org/problems/ball-coloring3450/1
# User function Template for python3
class Solution:
    def noOfWays(self, n):
        # code here
        return n*n - n+2


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.noOfWays(n))
# } Driver Code Ends
