"""
Only the first (intLength + 1) / 2 characters matter. T
he remaining characters are just a reflection.

Say intLength == 7, so we consider only 4 characters. 
The minimum number is 1000 and maximum - 9999.

Therefore, we can have 9999 - 1000 + 1 == 9000 palindromes. 
To find out the palindrome, we add a q - 1 to the minimum number, reverse, and concatenate.

For example, for query 8765, the base number is 1000 + 8765 - 1 == 9764. 
Concatenating it with 679, we get 9764679 as the result.
"""
queries = [1, 2, 3, 4, 5, 90]
intLength = 4


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        start = 10**((intLength+1)//2 - 1)
        end = 10**((intLength + 1) // 2)
        mul = 10**(intLength//2)
        ans = []
        for q in queries:
            if start+q > end:
                ans.append(-1)
                continue
            t = str(int(start+q-1))
            m = t[::-1]
            m = m[intLength % 2:]
            ans.append(int(t+m))
        return ans
