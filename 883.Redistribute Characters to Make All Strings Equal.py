# Redistribute Characters to Make All Strings Equal

words = ["abc","aabc","bc"]

def makeEqual(words):
    counts = {}
    
    for word in words:
        for c in word:
            counts[c] = counts.get(c, 0) + 1
    
    n = len(words)
    for val in counts.values():
        if val % n != 0:
            return False
    
    return True


print(makeEqual(words))
