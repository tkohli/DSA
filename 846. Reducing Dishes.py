# Reducing Dishes
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Intuition
        If we cook some dishes,
        they must be the most satisfied among all choices.

        Another important observation is that,
        we will cook the dish with small satisfication,
        and leave the most satisfied dish in the end.

        Explanation
        We choose dishes from most satisfied.
        Everytime we add a new dish to the menu list,
        all dishes on the menu list will be cooked one time unit later,
        so the result += total satisfaction on the list.
        We'll keep doing this as long as A[i] + total > 0.
        """
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res
        