edges = [[1, 2], [1, 3], [2, 3]]
# union find by rank
parent = [i for i in range(len(edges)+1)]
rank = [1 for i in range(len(edges)+1)]
# find first parent


def find(n):
    p = parent[n]
    while p != parent[p]:
        p = parent[p]
