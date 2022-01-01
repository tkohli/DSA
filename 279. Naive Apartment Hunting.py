# blocks are dict

def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestDistance = min(closestDistance, abs(i-j))
            maxDistanceAtBlocks[i] = max(
                maxDistanceAtBlocks[i], closestDistance)
    return getIdxAtMinValue(maxDistanceAtBlocks)


def getIdxAtMinValue(array):
    minValueIDx = 0
    minValue = float("inf")
    for i in range(len(array)):
        current = array[i]
        if minValue > current:
            minValue = current
            minValueIDx = i
    return minValueIDx


print(apartmentHunting([
    {
      "gym": False,
      "school": True,
      "store": False
      },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
], ["gym", "school", "store"]))
