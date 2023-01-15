from collections import defaultdict
s1 = "parker"
s2 = "morris"
baseStr = "parser"

dct = {}
for i in range(len(baseStr)):
    if baseStr[i] not in dct:
        dct[baseStr[i]] = min(s1[i], s2[i])
    else:
        dct[baseStr[i]] = min(s1[i], s2[i], dct[baseStr[i]])
ans = ""
for ch in baseStr:
    ans += dct[ch]
print(ans, dct)
# mare
