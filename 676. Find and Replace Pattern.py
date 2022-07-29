words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
# Output: ["mee","aqq"]

"""
we make a map for abb and mee where we map a->m, m->a, b->e, and e->b
then check if values match or not
"""
# def match(word, pattern):
#     m1, m2 = {}, {}
#     for w, p in zip(word, pattern):
#         if w not in m1:
#             m1[w] = p
#         if p not in m2:
#             m2[p] = w
#         if (m1[w], m2[p]) != (p, w):
#             return False
#     return True


def match(word):
    m1, m2 = {}, {}
    for w, p in zip(word, pattern):
        if w not in m1:
            m1[w] = p
        if p not in m2:
            m2[p] = w
        if (m1[w], m2[p]) != (p, w):
            return False
    return True


print([word for word in words if match(word)])

ans = []
for word in words:
    dp = {}
    dw = {}
    for i in range(len(pattern)):
        p = pattern[i]
        w = word[i]
        if p in dp and w != dp[p]:
            break
        elif w in dw and dw[w] != p:
            break
        else:
            dp[p] = w
            dw[w] = p
    else:
        ans.append(word)
