# Count of Smaller Numbers After Self
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        ans = []

        for num in nums[::-1]:
            n = SortedList.bisect_left(s, num)
            ans.append(n)
            s.add(num)
        return ans[::-1]
