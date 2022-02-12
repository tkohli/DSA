from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            # print(0)
            return 0
        # using this we will not need to implement start of dct vals eg. dct[ch] = 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):  # to generate all pattern
                pattern = word[:j]+'*'+word[j+1:]
                neighbor[pattern].append(word)
        print(neighbor)
        visited = set([beginWord])  # add
        queue = [beginWord]
        result = 1
        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)
                if current == endWord:
                    return result
                for j in range(len(current)):  # to generate all pattern
                    pattern = current[:j]+'*'+current[j+1:]
                    for newWord in neighbor[pattern]:
                        if newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)

            result += 1
        return 0
        # print(result)
