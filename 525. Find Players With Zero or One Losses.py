class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = DefaultDict(int)
        loser = DefaultDict(int)
        for win,los in matches:
            winner[win]+=1
            loser[los]+=1
        print(winner,loser)
        ans = []
        tmp = set()
        tmp2 = set()
        for val,count in winner.items():
            if val not in loser:
                tmp.add(val)
            
            elif loser[val]==1:
                tmp2.add(val)
        for val,count in loser.items():
            if count==1 and val not in tmp2:
                tmp2.add(val)
        tmp = list(tmp)
        tmp.sort()
        tmp2 = list(tmp2)
        tmp2.sort()
        return [tmp,tmp2]