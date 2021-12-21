"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five != 0:
                ten += 1
                five -= 1
            elif bill == 20 and five != 0 and ten != 0:
                ten -= 1
                five -= 1
            elif bill == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
