
"""
i/p = nums = [6 4 7 3 2 7 6 2]
o/p => [12, 7 ,6] 
so i have tried to do this based on it's own manuplation
so let's try stack  
"""
nums = [6,4,7,3,2,7,6,2]

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        import math
        n = len(nums)
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack)>=2:
                if math.gcd(stack[-1],stack[-2])>1:
                    stack.append(math.lcm(stack.pop(),stack.pop())) 
                else:
                    break
        return stack