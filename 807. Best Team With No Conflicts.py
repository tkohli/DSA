# Best Team With No Conflicts
"""
Nice question - if try to brute fore it usinging recursion it would give us TLE
                even using memeoization is not that optimized. Diving a little deeper

we can see that this question 
"""
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # [1,4,9,14,19]# scores is our dp
        # [1,3,5,10,15] 
        # [1,2,5, 4, 3]
        team = list(zip(ages,scores))
        team.sort()
        n = len(team)
        lis = [team[i][1] for i in range(n)]
        
        for i in range(1,n):
            for j in range(i):
                if team[i][1]>=team[j][1]:
                    lis[i] = max(lis[i],lis[j]+team[i][1])
        return max(lis)