import collections


nums = [2,2,3,3,3,4]
"""
We first sort this array and then find it counter 
then find its val that it will give when we use it 
it will become similar to house robber just we see 
if val was val-1 or val+1 then we skip
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1

        ans = [0]*(max(nums)+1)
        for key,val in count.items():

            ans[key] = (key*val)

        print(ans)

        # house robber :)
        rob1 = 0
        rob2 = 0
        for num in ans:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
# we can use only 2 var for the taskato improve our 
# space complexity
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        from collections import Counter
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0,0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            if i>0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 =max(earn1+curEarn,earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 =earn2+curEarn
                earn1 = temp
        return earn2