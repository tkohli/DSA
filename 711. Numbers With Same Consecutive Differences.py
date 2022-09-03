# Numbers With Same Consecutive Differences
n = 3
k = 7
# Output: [181, 292, 707, 818, 929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

"""
We can do this using recursion easily steps would be 
We could implement the recursive function in the following steps:

As a base case, when N=0 i.e. no more remaining digits to complete, 
we could return the current num as the result.

Otherwise, there are still some remaining digits to be added to the 
current number, e.g. 13. There are two potential cases to explore, 
based on the last digit of the current number which we denote as tail_digit.

Adding the difference K to the last digit, i.e. tail_digit + K.

Deducting the difference K from the last digit, i.e. tail_digit - K.

If the result of either above case falls into the valid digit range 
(i.e. [0, 9][0,9]),we then continue the exploration by invoking the 
function itself.

Once we implement the DFS(N, num) function, we then simply call this 
function over the scope of [1, 9][1,9], i.e. the valid digits for the 
highest position.
"""


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]

        ans = []

        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)
