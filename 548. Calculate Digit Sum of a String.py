class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = ""
            for i in range(0, len(s), k):
                tmp += str(sum(int(j) for j in s[i:i+k]))
            s = tmp
        return s
