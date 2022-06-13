"""
1. 3 sum
naive solution -> O(n^3) Time and O(1) Space basic 3 loops might get TLE
Optimization -> O(n^2) Time and O(1) Space after sorting
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        if len(nums) < 3:
            return []
        i = 0
        while i < len(nums) - 2:
            while len(nums) > i > 0 and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    res.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                if target < 0:
                    j += 1
                if target > 0:
                    k -= 1
            i += 1
        return res


"""
2. Different Ways to Add Parenthese  
Amazon question easy to hoga nhi par simple recursion hai 
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(n, op, m):
            n = int(n)
            m = int(m)
            if op == '+':
                return (n+m)
            if op == '-':
                return (n-m)
            if op == '*':
                return (n*m)

        def helper(l, r):
            ans = []
            for i in range(l, r):
                if expression[i] in '+-*/':
                    ans += [calc(le, expression[i], ri) for le in helper(l, i)
                            for ri in helper(i+1, r)]
            return ans if len(ans) != 0 else [int(expression[l:r])]

        return helper(0, len(expression))


"""
3. Min Stack -> just use an extra stack to keep track of min val :)
Simple Implementation only if seen
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []

    def push(self, val: int) -> None:
        if self.minst != []:
            if self.minst[-1] > val:
                self.minst.append(val)
            else:
                self.minst.append(self.minst[-1])
        else:
            self.minst.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.minst.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]


"""
3. Remove element

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, 
with the first two elements of nums being 2.
It does not matter what you leave beyond the 
returned k (hence they are underscores).
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j = len(nums)-1
        i = 0
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                k += 1
                i += 1
        return k


"""
Extra : Edit Distance 
Naive to banta hai par optimization is tricky
"""


def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    even = [x for x in range(len(small)+1)]
    odd = [None for x in range(len(small)+1)]
    for i in range(1, len(big)+1):
        current = even
        prev = odd
        if i % 2 == 1:
            current = odd
            prev = even
        current[0] = i
        for j in range(1, len(small)+1):
            if small[j-1] == big[i-1]:
                current[j] = prev[j-1]
            else:
                current[j] = 1+min(prev[j-1], prev[j], current[j-1])
    return even[-1] if len(big) % 2 == 0 else odd[-1]
