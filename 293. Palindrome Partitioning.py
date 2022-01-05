def partition(s):
    """
   :type s: str
   :rtype: List[List[str]]
   """
    ret = []
    for i in range(1, len(s)+1):
        if s[:i] == s[i-1::-1]:
            for rest in partition(s[i:]):
                ret.append([s[:i]]+rest)
    if not ret:
        return [[]]
    return ret


print(partition("aab"))
