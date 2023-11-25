# Sum of Absolute Differences in a Sorted Array

 nums = [1,4,6,8,10]


def getSumAbsoluteDifferences(nums):
    n = len(nums)
    total_sum = sum(nums)
    left_sum = 0
    ans = []

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        
        left_count = i
        right_count = n - 1 - i
        
        left_total = left_count * nums[i] - left_sum
        right_total = right_sum - right_count * nums[i]

        ans.append(left_total + right_total)
        left_sum += nums[i]
    
    return ans

print(getSumAbsoluteDifferences(nums))
