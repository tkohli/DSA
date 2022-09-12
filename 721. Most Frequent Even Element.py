class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cnt = Counter(nums)
        dct = defaultdict(list)
        curMax = -1
        for k, v in cnt.items():
            if k % 2 == 0:
                dct[v].append(k)
                curMax = max(curMax, v)
        if curMax != -1:
            return min(dct[curMax])
        return -1
