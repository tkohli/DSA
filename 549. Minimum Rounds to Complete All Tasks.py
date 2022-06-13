class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = defaultdict(int)
        for n in tasks:
            d[n] += 1

        ans = 0
        for count in d.values():
            if count == 1:
                return -1
            rem = count % 3
            div = count // 3
            if rem == 0:
                ans += div
            else:
                ans += (div + 1)

        return ans
