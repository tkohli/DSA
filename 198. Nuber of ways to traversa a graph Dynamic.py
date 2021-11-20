def numberOfWaysToTraverseGraph(width, height):
    ways = [[0 for _ in range(width+1)]for _ in range(height+1)]
    for h in range(height+1):
        for w in range(width+1):
            if h==1 or w==1:
                ways[h][w] = 1
            else:
                ways[h][w] = ways[h+1][w]+ways[h][w+1]

    # Write your code here.
    return ways[-1][-1]
