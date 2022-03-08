class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #O(n^2) Time and O(n) space beacuse of slicing
        n = len(needle)

        for i in range(len(haystack)-n+1):
            if needle == haystack[i:i+n]:
                return i

        return -1


haystack = "hello"
needle = "ll"



# sliding window
n = len(haystack)
m = len(needle)
i = 0
j = 0
for i in range(n-m+1):
    if haystack[i]==needle[j]:
        j+=1
    if j == m-1:
        # return i
        print(i)
    else:
        j = 1













