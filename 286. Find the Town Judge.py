from collections import defaultdict


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        a = {}
        dct = defaultdict(list)
        judgeTrust = defaultdict(lambda: 0, a)
        for i in range(len(trust)):
            dct[trust[i][0]].append(trust[i][1])
            judgeTrust[trust[i][1]] += 1
        # print(dct, judgeTrust)
        judge = -1
        for i in range(1, n+1):
            if dct[i] == []:
                if judgeTrust[i] == n-1:
                    return i
        return -1
