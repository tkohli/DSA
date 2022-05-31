class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 2 ** k
        got = set()
        temp = ""
        for i in range(k, len(s)+1):
            temp = s[i-k:i]
            if temp not in got:
                got.add(temp)
                need -= 1
            if need == 0:
                return True

        return False

        # got = {s[i - k : i] for i in range(k, len(s) + 1)}
        # return len(got) == 2**k
