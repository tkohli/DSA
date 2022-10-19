# 2423. Remove Letter To Equalize Frequency
from sortedcontainers import SortedList
from typing import Counter


class SolutionA:
    def equalFrequency(self, word: str) -> bool:
        """
        word = "aazz"

        We were given words and in this alot of approaches were wrong 
        we could have simply erased one char and then check if string 
        is satisfying the condition.
        """
        c = Counter(word)
        for i in word:
            c[i] -= 1

            s = []
            for j in c.values():
                if j:
                    s.append(j)
            if len(set(s)) == 1:
                return True

            c[i] += 1
        return False


# 2424. Longest Uploaded Prefix
class LUPrefix:
    """
    This was simple but yet complicated question we could have 
    This implementation is good way to keep track of all values and that too in 
    max value order 
    """

    def __init__(self, n: int):
        self.cur = [False]*n
        self.ans = 0

    def upload(self, video: int) -> None:
        self.cur[video-1] = True
        while 0 <= self.ans < len(self.cur) and self.cur[self.ans]:
            self.ans += 1

    def longest(self) -> int:
        return self.ans


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()


# 2425. Bitwise XOR of All Pairings
# Tears
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        A naive solution would five TLE so we use some properties
        If the length of nums1 is m and the length of nums2 is n, then each 
        number in nums1 is repeated n times and each number in nums2 is repeated m times.

        Explanation
        If B.length is even,
        ai will xor even times,
        and equal to 0.

        If B.length is odd,
        ai will xor odd times,
        and equal to ai.

        Same for bi

        If A.length is even and B.length is even,
        res = 0

        If A.length is odd and B.length is even,
        res = B[0] ^ B[1] ^ ...

        If A.length is even and B.length is odd,
        res = A[0] ^ A[1] ^ ...

        If A.length is even and B.length is even,
        res = A[0] ^ A[1] ^ ... ^ B[0] ^ B[1] ^ ...

        """
        a = 0
        if len(nums2) % 2:
            for i in nums1:
                a ^= i
        if len(nums1) % 2:
            for i in nums2:
                a ^= i
        return a


# 2426. Number of Pairs Satisfying Inequality


class Solution:
    def numberOfPairs(self, nums1, nums2, diff: int) -> int:
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        q = SortedList([a[0]])
        res = 0
        for i in range(1, n):
            j = q.bisect_right(a[i] + diff)
            res += j
            q.add(a[i])
        return res
