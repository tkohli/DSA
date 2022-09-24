from collections import deque


N = 8
arr = [3, 22, 5, 8, 11, 26, 20, 29,
       17, 4, 19, 7, 27, 1, 21, 9]
moves = [-1 for i in range(35)]
vis = [False for i in range(35)]

i = 0
while(i < 2*N):
    moves[arr[i]] = arr[i+1]
    i += 2
print(moves)
q = deque()
q.append([1, 0])
vis[1] = True
while(len(q)):
    p = q.popleft()
    ii = p[0]
    ss = p[1]
    if(ii == 30):
        break
    for i in range(ii+1, ii+7):
        if(i > 30):
            break
        pp = [0]*2
        if(vis[i] == False):
            vis[i] = True
            pp[1] = ss + 1
            if(moves[i] != -1):
                pp[0] = moves[i]
            else:
                pp[0] = i
            q.append(pp)
print(p[1])
# return p[1]
