# Maximum Number of Balls in a Box
"""
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.



Example 1:

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
"""


def countBalls(self, lowLimit, highLimit):
      """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
       def sumDigit(digit):
            sum = 0
            while digit:
                sum += digit % 10
                digit = digit//10
                # digits = list(str(num))
            # for digit in digits:
            #     sum += int(digit)
            return sum
        dict = {}
        for i in range(lowLimit, highLimit+1):
            sum = sumDigit(i)
            if sum in dict:
                dict[sum] += 1
            else:
                dict[sum] = 1

        return max(dict.values())
