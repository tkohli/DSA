s = "abcde"
words = ["a", "bb", "acd", "ace"]


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans, mappings = 0, defaultdict(list)
        for index, char in enumerate(s):
            mappings[char].append(index)
        for word in words:
            prev, found = -1, True
            for c in word:
                tmp = bisect.bisect(mappings[c], prev)  # return the index
        # where to insert item x in list a, assuming a is sorted binary search -> log n
        # print(tmp)  # 7
        # print(ch, mappings[ch][tmp])
                if tmp == len(mappings[c]):
                    found = False
                    break
                else:
                    prev = mappings[c][tmp]
            ans += found == True
        return ans
