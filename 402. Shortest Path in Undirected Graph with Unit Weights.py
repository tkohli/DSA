graph = [[1, 2, 3], [0], [0], [0]]

# Convert this to an adjacency matrix
adj = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
n = len(graph)
source = 0

distance = [float("inf") for _ in range(n)]

queue = [source]
distance[source] = 0

while queue:
    node = queue.pop(0)
    for neighbor in adj[node]:
        if distance[neighbor] > distance[node]+1:
            distance[neighbor] = distance[node]+1
            queue.append(neighbor)

print(distance)
