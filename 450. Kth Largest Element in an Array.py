"""
1. sort it and the return kth largest solution # nlog n
2. heap it nice and clean but O(n) and the del k operation. klogn 
3. O(n) avg but O(n^2) worst Quick select
partition it based on random pivot
"""
nums = [3,2,1,5,6,4]
k = 2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k 

        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]

            if p>k:
                return quickSelect(l,p-1)
            elif p<k:
                return quickSelect(p+1,r)
            return nums[p]
            
        return quickSelect(0,len(nums)-1)