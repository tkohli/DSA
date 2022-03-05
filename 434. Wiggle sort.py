"""
nums[0] <= nums[1] >= nums[2] <= nums[3]....
Input: [3, 5, 2, 1, 6, 4]

So we can do this by simply sorting it out
and then swapping it but it will take n log n time

Think about some optimization

use 2 pointer and keep checking the val If not matches 
then just swap them
3 5 2 1 6 4
3 5 1 2 6 4 swap 1 and 2
3 5 1 6 2 4 swap 2 and 6
At odd number value should be higher then prev val
at even should be less the prev
"""

nums = [3,5,2,1,6,4]
for i in range(len(nums)):
    if i%2 == 1:
        if nums[i]<nums[i-1]:
            # swap
            nums[i], nums[i-1]= nums[i-1], nums[i] 
    else:
        if nums[i]>nums[i-1]:
            # swap
            nums[i], nums[i-1]= nums[i-1], nums[i]