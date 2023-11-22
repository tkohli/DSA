# Diagonal Traverse II
nums = [[1,2,3],[4,5,6],[7,8,9]]

from collections import defaultdict


def findDiagonalOrder(nums):
    groups = defaultdict(list)
    for row in range(len(nums) - 1, -1, -1):
        for col in range(len(nums[row])):
            diagonal = row + col
            groups[diagonal].append(nums[row][col])
            
    ans = []
    curr = 0
    
    while curr in groups:
        ans.extend(groups[curr])
        curr += 1

    return ans


print(findDiagonalOrder(nums))
