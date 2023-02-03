# Verifying an Alien Dictionary
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {}
        for i,ch in enumerate(order):
            orderIndex[ch] = i
        # main idea is to check adjacent words if they satisfy condition then we continue else return False

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                    # hello, he -> return False
                if w1[j]!=w2[j]:
                    if orderIndex[w1[j]]>orderIndex[w2[j]]:
                        return False
                    break
        return True