class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dct = Counter(nums)
        pair = left = 0
        for k,v in dct.items():
            if v%2==1:
                left+=1
            pair+=(v//2)
        return [pair,left]