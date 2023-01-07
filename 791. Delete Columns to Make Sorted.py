class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # O(nm) time and O(1) sapce
        cnt = 0
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(len(strs)):
                if tmp > strs[j][i]:
                    cnt += 1
                    break
                tmp = strs[j][i]
        return cnt

        # O(nm log(m)) time and O(m) sapce
        # cnt = 0
        # for i in range(len(strs[0])):
        #     tmp = ""
        #     for j in range(len(strs)):
        #         tmp+=strs[j][i]
        #     cnt += (sorted(tmp)!=list(tmp))

        # return cnt

        # O(nm log(m)) time and O(nm) sapce
        # strs[::] = zip(*strs)
        # # print(strs)
        # ans = 0
        # for col in strs:
        #     if list(col) != sorted(col):
        #         ans += 1

        # return ans
