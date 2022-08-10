class Solution:  # O(n) Time and O(n) space
    def countVowelPermutation(self, n: int) -> int:
        """
        Let dfs to try all possible result result. When we reach a valid 
        possible way, return 1. Use memoization to cache the sub-problem 
        result, so it doesn't need compute again.
        """
        map = {
            '.': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        @lru_cache(None)
        def dp(i, last):
            if i == n:
                return 1
            ans = 0
            for nxt in map[last]:
                ans = (ans + dp(i + 1, nxt)) % 1_000_000_007
            return ans

        return dp(0, '.')


class Solution:  # O(n) Time and O(1) space
    def countVowelPermutation(self, n: int) -> int:
        # Convert the Next relationship into Previous Relationship,
        # then do Bottom Up DP.
        a = e = i = o = u = 1
        MOD = 10**9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u), (a +
                                          i), (e + o), i, (i + o)
        return (a + e + i + o + u) % MOD
