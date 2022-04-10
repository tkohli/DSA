class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        odd, ans = 0, 0

        for x in d:
            if d[x] % 2:
                odd += 1
            ans += d[x]

        return min(ans, ans - odd + 1)
#         cnt = Counter(s)
#         odd = 0
#         ans = 0
#         for x in cnt:
#             if cnt[x] % 2 == 0:
#                 odd += 1
#             ans += cnt[x]


#         return min(ans, ans - odd + 1)
