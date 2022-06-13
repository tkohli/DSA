"""
Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], 
we get "abadcdbc". 
Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" 
after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", 
and "abdcdbcc", although obtainable, have only 3
 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to 
get more than 4 subsequences "ac" by adding 
only one character.


_________________________Solution_____________________________
Only way to maximise the number of subsequence is 
to either add pattern[0] at the start of the given string 
or to add pattern[1] at end of the given string.
Example: text = "aabb", pattern = "ab"

aabb -> count_a = 1, count_b = 0, total = 0
aabb -> count_a = 2, count_b = 0, total = 0
aabb -> count_a = 2, count_b = 1, total = 2
aabb -> count_a = 2, count_b = 2, total = 4
"""


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        total = countA = countB = 0
        for c in text:
            if c == pattern[1]:
                total += countA
                countB += 1
            if c == pattern[0]:
                countA += 1

        total += max(countA, countB) + countA
        return total
