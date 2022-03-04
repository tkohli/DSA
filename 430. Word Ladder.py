from collections import defaultdict


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]



"""
hit - > h*t , *it, hi* where * is wildcard
then in h*t -> hot, from h*t, *ot, ho*
then in *ot -> dot then from do*
we get dog then finally we get cog with 5 steps
Easier if we follow all steps 
"""

if endWord not in wordList:
    pass
    # return 0

dct = defaultdict(list)
wordList.append(beginWord)
for word in wordList:
    for i in range(len(word)):
        pattern = word[:i]+'*'+word[i+1:]
        dct[pattern].append(word)
# now keep the track of word see to avoid cycles
visited = set([beginWord])
queue = [beginWord]
count = 1

# now do bfs 
while queue:
    for i in range(len(queue)):
        current = queue.pop(0)
        if current == endWord:
            # return count
            print(count)
            break
        for j in range(len(current)):
            pattern = current[:j]+'*'+current[j+1:]
            for word in dct[pattern]:
                if word not in visited:
                    visited.add(word)
                    queue.append(word)
    count+=1

