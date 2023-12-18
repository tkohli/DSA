# Maximum Product Difference Between Two Pairs

nums = [5,6,2,7,4]

def maxProductDifference(nums):
    biggest = 0
    second_biggest = 0
    smallest = inf
    second_smallest = inf
    
    for num in nums:
        if num > biggest:
            second_biggest = biggest
            biggest = num
        else:
            second_biggest = max(second_biggest, num)
            
        if num < smallest:
            second_smallest = smallest
            smallest = num
        else:
            second_smallest = min(second_smallest, num)
    
    return biggest * second_biggest - smallest * second_smallest


print(maxProductDifference(nums))

def maxProductDifference(num):
    nums.sort()
    return abs((nums[0]*nums[1]) - (nums[-1]*nums[-2]))


print(maxProductDifference(nums))
