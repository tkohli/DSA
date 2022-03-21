"""
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at 
most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
because it splits s into less parts.

--------------Solution--------------
We start by taking lastseen index of all char so we know when to separate them
after that loop through array and check max index of all element 
then separate them based on start and end idx
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for idx, ch in enumerate(s):
            lastSeen[ch] = idx
        anchor = j = 0  # start and end of str
        ans = []
        for idx, ch in enumerate(s):
            j = max(j, lastSeen[ch])
            if j == idx:
                ans.append(idx-anchor+1)
                anchor = idx+1
        return ans
