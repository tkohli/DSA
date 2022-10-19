# https://leetcode.com/contest/weekly-contest-314/problems/the-employee-that-worked-on-the-longest-task/
# simple
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        ans = [0, 0]
        for usr, end in logs:
            if ans[1] == end-prev:
                ans[0] = min(ans[0], usr)
            if ans[1] < end-prev:
                ans = [usr, end-prev]
            prev = end
            # print(ans)
        return ans[0]

# https://leetcode.com/contest/weekly-contest-314/problems/find-the-original-array-of-prefix-xor/
# simple but tricky


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [0]*len(pref)
        ans[0] = pref[0]
        c = 0
        for i, ele in enumerate(pref):
            ans[i] = c ^ pref[i]
            c = ans[i] ^ c

        return ans
