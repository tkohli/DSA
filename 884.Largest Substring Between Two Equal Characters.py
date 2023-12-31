# Largest Substring Between Two Equal Characters

s = "abca"

def maxLengthBetweenEqualCharacters(s):
    ans = -1
    dct = {}
    for i in range(len(s)):
        if s[i] in dct:
            ans = max(ans, i-dct[s[i]]-1)
        else:
            dct[s[i]]= i
    return ans


print(maxLengthBetweenEqualCharacters(s))
