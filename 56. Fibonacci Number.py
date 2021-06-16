# Fibonacci Number
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""


def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n > 60:
        n = n % 60
    fibs = [0, 1]
    if n < 2:
        return (n)
    for i in range(n+3):
        fibs.append(fibs[-1]+fibs[-2])
    return (fibs[n-2]+fibs[n-1])
