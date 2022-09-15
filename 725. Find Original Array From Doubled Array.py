from typing import Counter

"""
Let's see a simple case
Assume all interger are positive, for example [2,4,4,8].
We have one x = 2, we need to match it with one 2x = 4.
Then one 4 is gone, we have the other x = 4.
We need to match it with one 2x = 8.
Finaly no number left.

Why we start from 2?
Because it's the smallest and we no there is no x/2 left.
So we know we need to find 2x

Explanation
Count all numbers.
Loop all numbers on the order of its absolute.
We have counter[x] of x, so we need the same amount of 2x wo match them.
If c[x] > c[2 * x], then we return []
If c[x] <= c[2 * x], then we repeatly do c[2 * x]-- and append x to result res
Don't worry about 0, it doesn't fit the logic above but it won't break our algorithme.

In case count[0] is odd, it won't get matched in the end.

In case count[0] is even, we still have c[0] <= c[2 * 0].
And we still need to check all other numbers.
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        for n in sorted(counter):
            if n == 0 and counter[0] % 2 == 1:
                return []

            if counter[n] > counter[n*2]:  # if source more than the derivatives return false
                return []
            if n:
                # remove derivatives, keep the source elements
                counter[n*2] -= counter[n]
            else:
                counter[n] //= 2

        # elements return the key where value is non-zero
        return list(counter.elements())

#         cnt, ans = Counter(arr), []
#         for num in sorted(arr, key = lambda x: abs(x)):
#             if cnt[num] == 0: continue
#             if cnt[2*num] == 0: return []
#             ans += [num]
#             if num == 0 and cnt[num] <= 1: return []
#             cnt[num] -= 1
#             cnt[2*num] -= 1

#         return ans
        # c = collections.Counter(A)
        # if c[0] % 2:
        #     return []
        # for x in sorted(c):
        #     if c[x] > c[2 * x]:
        #         return []
        #     c[2 * x] -= c[x] if x else c[x] // 2
        # return list(c.elements())
