class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def rec(idx,temp,ans):
            if sum(temp) == target:
                ans.append(temp)
                return ans
            elif sum(temp) > target:
                return ans
            
            for i in range(idx,n):
                ans = rec(i,temp+[candidates[i]],ans)
            
            return ans 
     
        return rec(0,[],[])