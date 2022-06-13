class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num = [[sum(m), i] for i, m in enumerate(mat)]
        num.sort()
        ans = [i[1] for i in num[:k]]
        return ans
