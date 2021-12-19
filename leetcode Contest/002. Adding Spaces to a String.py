class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        out = []
        start = 0
        for space in spaces:
            out.append(s[start:space])
            start = space
        out.append(s[start:])
        return " ".join(out)


# for i, sp in enumerate(spaces):
#     s.insert(i+sp, " ")
# print("".join(s))
"""
This way goes TLE
"""
# out = []
# start = 0
# for sp in spaces:
#     out.append(s[start:sp])
#     start = sp
# out.append(s[start:])

# print(out)
# print(" ".join(out))

"""
More ways todo
l = []
cur = 0
for j, i in enumerate(s):
    if cur < len(spaces) and spaces[cur] == j:
        l.append(' ')
        cur += 1
    l.append(i)
return ''.join(l)
"""
