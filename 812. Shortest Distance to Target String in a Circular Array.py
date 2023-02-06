# Shortest Distance to Target String in a Circular Array
"""
We can solve this in 2 pass or we can can do it in single pass
Do a for loop from 0 to n
then from the question "Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words."
use these lines.
"""
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n):
            if words[(startIndex+i) % n] == target or words[(startIndex-i+n)%n] == target:
                return i
        return -1