# Find Duplicate in Array
"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in 
linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumberMySolution(self, A):
        """
        This loop run exactly n-1 times so that we pass the condition 
        of linear time less than O(n).
        """
        N = list(A)
        N.sort()
        nst = N[0]
        for n in N[1:]:
            if nst == n:
                return nst
            else:
                nst = n
        return -1
    def repeatedNumberStandard(self, A):
        lenA = len(A)
        temp = [0]*lenA
        for i in A:
            if temp[i - 1]:
                return i
            else:
                temp[i - 1] = 1
        return -1
    
    def repeatedNumberFastest(self, A):
        sumOfList = sum(A)
        n = len(A)
        sumOfRange = int(n * (n + 1) / 2) - n
        return sumOfList - sumOfRange
        
