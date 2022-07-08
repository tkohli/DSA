class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        charSet = [set(word) for word in words]
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if charSet[i] & charSet[j]:  # checking for intersection
                    continue
                ans = max((len(words[i])*len(words[j])), ans)
        return ans


"""
Using bitset as we are making charset for processing this but we can make a bitset
which will have less comparision time  
"""
