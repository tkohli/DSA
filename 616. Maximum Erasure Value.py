class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i,j,s,n,total = 0,0,set(),len(nums),0
        ans = 0
        while j<n:
            if nums[j] not in s:
                s.add(nums[j])
                total += nums[j]
                j+=1
                ans = max(ans,total)
            else:
                s.remove(nums[i])
                total -= nums[i]
                i+=1
        return ans 
