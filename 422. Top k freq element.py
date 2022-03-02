"""
nums = [1,1,1,2,2,3]
k = 2
o/p = [1,2]

Can be solved easily using dict or 
just sort it out then keep count
it will use n log n
even if we use maxHeap and the
find k for that also worst case we get k log n

So we use BUCKET SORT for n time and n space   

idx    0    1    2    3    ... 100
count  0    3    2    0         1


i(count)    0   1       2      3    4   5   6 (len(arr))
values      0   [100]   [2]   [1]   0   0   0
then loop reverse
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1

        for key,val in count.items():
            freq[val].append(key)

        ans = []
        for arr in reversed(freq):
            if arr==[]:
                continue
            for i in arr:
                ans.append(i)
                k-=1
                if k==0:
                    return ans