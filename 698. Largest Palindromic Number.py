class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')
        mid = max(count[i] % 2 * i for i in count)
        return (res + mid + res[::-1]) or '0'
#         c = Counter(num)

#         start = []
#         for d in map(str, reversed(range(10))):
#             if d == "0" and len(start) == 0:
#                 break
#             start.extend([d] * (c[d] // 2))
#             c[d] = c[d] % 2

#         center = ""
#         for d in map(str, reversed(range(10))):
#             if c[d]:
#                 center = d
#                 break

#         return "".join(start) + center + "".join(start[::-1])
