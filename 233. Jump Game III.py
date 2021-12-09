class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        seen, temp = set(), [start]
        while temp:
            i = temp.pop()
            if arr[i] == 0:
                return True
            else:
                seen.add(i)
            prev = i - arr[i]
            next = i + arr[i]
            if 0 <= prev < len(arr) and prev not in seen:
                temp.append(i - arr[i])
            if 0 <= next < len(arr) and next not in seen:
                temp.append(next)
        return False
# arr = [3, 0, 2, 1, 2]
# start = 2
# n = len(arr)
# num1 = start
# num2 = start
# nums = []
# while n >= 0:
#     if arr[num1] == 0 or arr[num2] == 0:
#         print(True)
#     num1 += arr[num1]
#     num2 -= arr[num2]
#     num2 = abs(num2)
#     num1 = num1 % len(arr)
#     num2 = num2 % len(arr)
#     n -= 1
# print(False)
