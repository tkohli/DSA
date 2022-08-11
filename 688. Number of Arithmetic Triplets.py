class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        count = 0
        for num in nums:
            if num-diff in seen and num-diff*2 in seen:
                count += 1
            seen.add(num)
        return count

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[j]-nums[i] == diff:
        #             for k in range(j,len(nums)):
        #                 if nums[k]-nums[j] == diff:
        #                     count+=1
        # return count
