# Valid Ip Addresses
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""
class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        n = len(s)
        ans = list()
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if 1 <= len(s[:i]) <= 3 and ((s[:i][0] == '0' and len(s[:i]) == 1) or (s[:i][0] != '0')) and 0 <= int(s[:i]) <= 255 \
                    and 1 <= len(s[i:j]) <= 3  and ((s[i:j][0] == '0' and len(s[i:j]) == 1) or (s[i:j][0] != '0')) and 0 <= int(s[i:j]) <= 255 \
                    and 1 <= len(s[j:k]) <= 3  and ((s[j:k][0] == '0' and len(s[j:k]) == 1) or (s[j:k][0] != '0')) and 0 <= int(s[j:k]) <= 255 \
                    and 1 <= len(s[k:]) <= 3  and ((s[k:][0] == '0' and len(s[k:]) == 1) or (s[k:][0] != '0')) and 0 <= int(s[k:]) <= 255:
                        ans.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])
        return sorted(ans)
