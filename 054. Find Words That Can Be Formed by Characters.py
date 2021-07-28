# Find Words That Can Be Formed by Characters
"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
"""


def countCharacters(self, words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    out = 0
    for word in words:
        if len(chars) < len(word):
            continue
            count = 0
            case = len(word)
            for i in word:
                if i not in chars:
                    break
                if (chars.count(i) >= word.count(i)):
                    count += 1
            if count == case:
                out += case
        return (out)
