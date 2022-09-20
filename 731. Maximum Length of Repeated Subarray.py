A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
# very similar to edit distance s


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = "".join([chr(x) for x in nums2])
        nums1_str = "".join([chr(x) for x in nums1])
        N = len(nums1_str)
        res = 0
        i = 0
        for j in range(1, N+1):
            if nums1_str[i:j] in nums2_str:
                res = max(res, j-i)
            elif i < j:
                i += 1

        return res

        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
        return max(max(row) for row in memo)
