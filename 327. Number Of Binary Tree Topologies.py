from random import randrange
from turtle import right


def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    number = 0
    for i in range(n):
        # right =
        left = numberOfBinaryTreeTopologies(i, cache)
        right = numberOfBinaryTreeTopologies(n-1-i, cache)
        number += left*right
    cache[n] = number
    return number
