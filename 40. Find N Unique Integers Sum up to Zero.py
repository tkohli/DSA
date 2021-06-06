#Find N Unique Integers Sum up to Zero
"""

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""
def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = []
        if n%2!=0:
            lst.append(0)
       
        
        for i in range(1,(n//2)+1):
            lst.append(i)
            lst.append(-i)
        return (lst)
        