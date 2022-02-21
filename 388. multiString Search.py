"""
We can solve this question using naive solution and then make partial
Trie solution then we can work on complete trie solution
O(ns+bs) time and O(ns) space complexity
"""


def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedString = {}
    for i in range(len(bigString)):
        findSmallStringInBigString(bigString, i, trie, containedString)
    return [string in containedString for string in smallStrings]


def findSmallStringInBigString(string, startIdx, trie, containedString):
    current = trie.root
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in current:
            break
        current = current[currentChar]
        if trie.endSymbol in current:
            containedString[current[trie.endSymbol]] = True


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        node = self.root
        for j in range(len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = string
