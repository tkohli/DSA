"""
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

if we make a normal decision tree and the we get 
repeated same set that sum up our target eg = [2,3,3] and [3,2,3] etc
which is not allowed so modified tree will be like in which we stop 
an element after it is seen
eg =                0
                /       \
        [2]               [0]
        /      \         /  \
    [2,2]        [2]   [3]  [0]
    /   \                   /   \
[2,2,2] [2,2]             [5]    [0]
So we are adding repeated element into left 
And it continuous like that
"""


res = []
candidates = [2,3,5]
target = 8

def dfs(i, cur, total):
    if total==target:
        res.append(cur.copy())
        return
    if total>target or i >= len(candidates):
        return # our base return case
    # now make 2 recusrive calls where add prev char to one
    # and increase i to second part
    cur.append(candidates[i])
    dfs(i,cur,total+candidates[i])
    cur.pop()
    dfs(i+1, cur, total)


dfs(0,[],0)
print(res)