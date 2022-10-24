intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
A = []
for a, b in intervals:
    A.append([a, 1])
    A.append([b + 1, -1])
res = cur = 0
A.sort()
print(A)
