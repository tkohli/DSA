"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
_______________________
Solution 
So we can do this question in 2 ways we can use DP or just sort it based on difference of
cost of A ith city  - cost of B ith city
eg: 
[[10,20], [30,200], [400,50], [30,20]]
   -10      -170       350       10
After sorting it becomes
    -170      -10        10        350
[[30, 200], [10, 20], [30, 20], [400, 50]]
from the first half take Oth and from 2nd half we take 1st 

"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda cost: cost[0]-cost[1])
        ans = 0
        for i in range(len(costs)//2):
            ans += (costs[i][0] + costs[-i-1][1])
        return ans
