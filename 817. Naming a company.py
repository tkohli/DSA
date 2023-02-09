# Naming a Company

"""
    Initializing a defaultdict of set and an ans = 0 then
    store group the words by their initial letter in dct that is initial letter with suffixes
    eg. word coffee will be store like this c:{offee} similarly others words after that 
    Iterate over every pair of groups.For each group i and j, get the number of mutual suffixes
    that appears in both groups. so now we can swap every distinct suffix in group i with every distinct 
    suffix in group j, increment answer by 2 * (len(group[i]) - num_of_mutual) * (len(group[j]) - num_of_mutual)
    return answer
"""

# Time Complexity = O(n*m)   n - len(ideas)
# Space Complexity = O(n*m)  m - len(set)

from collections import defaultdict

ideas = ["coffee","donuts","time","toffee"]

def distinctNames(ideas):
    dct = defaultdict(set)
    ans = 0
    for idea in ideas:
        dct[idea[0]].add(idea[1:])
    seen = set()
    for k,v in dct.items():
        for ele ,val in dct.items():
            if k==ele or ele in seen:
                continue
            num_of_mutual = len(v & val)
            ans += 2* (len(v) - num_of_mutual) * (len(val) - num_of_mutual)
        seen.add(k)
    return ans

print(distinctNames(ideas))