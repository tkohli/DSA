class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

    # [1,1,2,  3,3, 4,4,8,8]
    #  l   r    m m l      r
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if (mid-1<0 or nums[mid]!=nums[mid-1]) and  (mid+1==len(nums) or nums[mid]!=nums[mid+1]):
                return nums[mid]

            if nums[mid]==nums[mid+1]:
                leftSize = mid
            else:
                leftSize = mid+1

            if leftSize %2 ==1:
                r = mid-1
            else:
                l = mid+1

        #     if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid+1]==nums[mid]):
        #         l = mid+1
        #     else:
        #         r = mid
        # return nums[l]