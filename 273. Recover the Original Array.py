"""
Alice had a 0-indexed array arr consisting of n positive integers. She chose an arbitrary positive integer k and created two new 0-indexed integer arrays lower and higher in the following manner:

lower[i] = arr[i] - k, for every index i where 0 <= i < n
higher[i] = arr[i] + k, for every index i where 0 <= i < n
Unfortunately, Alice lost all three arrays. However, she remembers the integers that were present in the arrays lower and higher, but not the array each integer belonged to. Help Alice and recover the original array.

Given an array nums consisting of 2n integers, where exactly n of the integers were present in lower and the remaining in higher, return the original array arr. In case the answer is not unique, return any valid array.
"""

import collections
nums = [97, 46, 43, 84, 64, 11, 41, 35, 88, 44, 52, 45, 66, 93, 58, 64, 79, 50, 21, 23, 85, 56, 94, 11, 60, 72, 63, 91, 43, 71, 33, 17, 79,
        73, 67, 51, 73, 61, 42, 62, 65, 87, 29, 58, 36, 78, 76, 54, 46, 84, 39, 37, 76, 1, 5, 47, 7, 37, 76, 82, 17, 40, 82, 78, 27, 57, 55, 70]
nums.sort()
mid = len(nums)//2
counter = {}
# for num in nums:
#     if num not in counter:
#         counter[num] = 0
#     counter[num] += 1
# counter = collections.Counter(nums)

# print(counter[5])
for i in range(1, mid+1):
    if nums[i] - nums[0] > 0 and (nums[i] - nums[0]) % 2 == 0:
        k = (nums[i]-nums[0])//2
        ans = []
        counter = collections.Counter(nums)
        # for num in nums:
        #     if num not in counter:
        #         counter[num] = 0
        #     counter[num] += 1
        for n in nums:
            if counter[n] == 0:
                continue
            if n+2*k in counter:
                if counter[n+2*k] == 0:  # not found corresponding number in higher list
                    break
            else:
                break
            ans.append(n + k)
            counter[n] -= 1  # remove n
            counter[n + 2 * k] -= 1
        if len(ans) == mid:
            print(ans)
#
