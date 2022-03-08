class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt = 0
        idx = 0
        for num in nums:
            if num <target:
                idx+=1
            if num == target:
                cnt+=1
            
        ans = []
        for i in range(cnt):
            ans.append(idx+i)
        return ans