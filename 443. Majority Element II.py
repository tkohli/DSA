class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        num1 = num2 = float('inf')
        c1 = c2 = 0

        for num in nums:
            
            if num1==num:
                c1+=1
            elif num2 == num:
                c2+=1
            elif c1 ==0:
                num1 = num
                c1=1
            elif c2 == 0:
                num2 = num
                c2=1
            else:
                c1-=1
                c2-=1
        res = []
        for x in [num1, num2]:
            if nums.count(x) > len(nums) // 3:
                res.append(x)
        return res