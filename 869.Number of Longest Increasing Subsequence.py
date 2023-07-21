# Number of Longest Increasing Subsequence

nums = [1,3,5,4,7]

def findNumberOfLIS(nums):
    n = len(nums)
    length = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = 0
                if length[j] + 1 == length[i]:
                    count[i] += count[j]
    
    max_length = max(length)
    result = 0
    
    for i in range(n):
        if length[i] == max_length:
            result += count[i]
    
    return result


print(findNumberOfLIS(nums))
