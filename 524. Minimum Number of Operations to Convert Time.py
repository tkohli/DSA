class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        t1 = int(current[0])*60 + int(current[1])
        correct = correct.split(":")
        t2 = int(correct[0])*60 + int(correct[1])
        time = abs(t2-t1)
        ans = 0
        for t in [60, 15, 5, 1]:
            tmp = time//t
            ans += tmp
            time -= tmp*t
        return ans
