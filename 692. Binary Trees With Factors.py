"""
https://leetcode.com/problems/binary-trees-with-factors/discuss/1107357/PythonGo-by-DP-w-Diagram
Sort A to make it in ascending order

Scan each root node value, and decompose it to all possible factors (i.e., the so-called child node value in binary tree).

Update the number of binary tree into dp table by dp[ x ] += dp[ y ] * dp[ x / y ]

Repeat step 2 and step 3 to build DP table in bottom-up order.

Finally, sum up the DP table's value and get the total count.

Don't forget to take the mod (10^9 + 7), which is defined by description.
"""


class Solution:
    def numFactoredBinaryTrees(self, A):

        # dictionary
        # key: root node value
        # value: number of binary tree
        dp = defaultdict(int)

        # keep A sorted in ascending order
        A.sort()

        constant, size = (10**9 + 7), len(A)

        # scan each possible root node value
        for i, cur_num in enumerate(A):

            # Case 1: cur_num as root with child nodes

            # scan each potential child node value
            for j in range(i):

                factor = A[j]
                quotient, remainder = divmod(cur_num, factor)

                # current (factor, quotient) pair are feasible to be child nodes
                if remainder == 0:
                    dp[cur_num] += dp[quotient] * dp[factor]

            # Case 2: cur_num as root without child nodes
            dp[cur_num] += 1

        return sum(dp.values()) % constant
