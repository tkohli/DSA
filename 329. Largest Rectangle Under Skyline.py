def largestRectangleUnderSkyline(buildings):
    pillarIdxs = []
    maxArea = 0
    for idx, height in enumerate(buildings+[0]):
        while len(pillarIdxs) != 0 and buildings[pillarIdxs[len(pillarIdxs)-1]] >= height:
            pillarheight = buildings[pillarIdxs.pop()]
            width = idx if len(pillarIdxs) == 0 else idx - \
                pillarIdxs[len(pillarIdxs)-1]-1
            maxArea = max(maxArea, pillarheight*width)
        pillarIdxs.append(idx)
    return maxArea


print(largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]))
