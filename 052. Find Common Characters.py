# Find Common Characters
"""
Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""


def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    letters = list(words[0])
    print("letters", letters)
    for i in range(1, len(words)):
        print(words[i])
        j = 0
        while j < len(letters):

            if letters[j] not in words[i]:
                letters.remove(letters[j])
                print(words[i], "removed")
            else:
                print(words[i], letters[j], "o")
                words[i] = words[i].replace(letters[j], "", 1)
                print(words[i], "changed")
                j = j+1
        print("letters", letters)
    return letters
    # Naive and slow
    # letters = list(words[0])
    # for alp in words[1:]:
    #     test = []
    #     alp = list(alp)
    #     print(letters, alp)
    #     for i in letters:
    #         if i in alp:
    #             test.append(i)
    #             alp.remove(i)
    #     letters = test
    #     print("common =", letters)
    # return (letters)


words = ["cool", "lock", "cook"]
print(commonChars(words))
# print(commonChars(["bella", "label", "roller"]))
