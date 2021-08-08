# Count And Say
"""
Problem Description

The count-and-say sequence is the sequence of integers beginning as follows: 
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11. 11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2, the sequence is 11.
"""
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A <= 0:
            return '' 
        seq = '1'
        for n in range(1, A):
            prev = seq
            seq = ''
            count = 1
            for i in range(1,len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    seq += str(count) + prev[i-1]
                    count = 1
            seq += str(count) + prev[-1]
        return seq
