n = 5
k = 73


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphabet = "0abcdefghijklmnopqrstuvwxyz"
        ans = ['a']*n
        val = n
        for i in reversed(range(n)):
            if val == k:
                break
            val -= 1  # removing a and then
            ans[i] = alphabet[min((k-val), 26)]
            val += min((k-val), 26)

        return "".join(ans)
