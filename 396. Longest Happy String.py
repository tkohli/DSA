import heapq
"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [[-a, 'a'], [-b, 'b'], [-c, 'c']]:
            if count != 0:
                heapq.heappush(maxHeap, [count, char])

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            # check is value is appearing for the third time
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, [count2, char2])

            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, [count, char])

        return res
