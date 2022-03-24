"""
Note that we can only take 2 people so no need for second while loop
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[r]+people[l] <= limit:
                l += 1
            r -= 1
            count += 1
        return count
