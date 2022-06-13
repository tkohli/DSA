"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
We can start by taking smallest str in strs and then 
go to all elements one by one to check their ans 


for optimization we can use trie TODO
"""
strs = ["flower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = ''
        l = float('inf')
        ans = ''

        for st in strs:
            if len(st) < l:
                l = len(st)
                small = st

        for i in range(len(small)):
            for j in range(len(strs)):
                tmp = strs[j]
                if small[i] != tmp[i]:
                    return ans
                if j == len(strs)-1:
                    ans += small[i]
        return ans
