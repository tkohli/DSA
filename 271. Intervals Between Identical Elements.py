from typing import DefaultDict
arr = [2, 1, 3, 1, 2, 3, 3]

pos = DefaultDict(list)
for i, x in enumerate(arr):
    pos[x].append(i)

# prefix array
pre = [0]*(len(arr))
# suffix array
suf = [0]*(len(arr))

ans = [0]*(len(arr))

for elem, l in pos.items():
    # traversing the positions of each element
    # for prefix
    for i in range(1, len(l)):
        pre[l[i]] = pre[l[i-1]] + i*(l[i]-l[i-1])

# for suffix
    for i in range(len(l)-2, -1, -1):
        suf[l[i]] = suf[l[i+1]] + (len(l)-1-i)*(l[i+1]-l[i])

for i in range(len(arr)):
    ans[i] += pre[i]+suf[i]
print(ans)
