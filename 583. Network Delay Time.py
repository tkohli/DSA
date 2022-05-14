times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2

dist = [float("inf") for _ in range(N)]
dist[K-1] = 0
for _ in range(N-1):
    for u, v, w in times:
        if dist[u-1] + w < dist[v-1]:
            dist[v-1] = dist[u-1] + w

print(dist)
