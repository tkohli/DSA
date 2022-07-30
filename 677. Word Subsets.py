from typing import Counter


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt = Counter(words2[0])
        for word in words2[1:]:
            tmp = Counter(word)
            for k, v in tmp.items():
                cnt[k] = max(cnt[k], v)  # will count frequency of all char
        ans = []
        for word in words1:
            tmp = Counter(word)
            found = True
            for k, v in cnt.items():
                if tmp[k] < v:
                    found = False
                    break
            if found:
                ans.append(word)
        return (ans)
