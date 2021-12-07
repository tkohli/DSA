def waterArea(heights):
    """
    check highest and lowest pillar 
    and then check water level for each tower 
    this is better than naive approach  
    """
    maxes = [0 for x in heights]
    # if len(heights)==0:
    #     return 0
    leftMax=0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax,height)
    rightMax=0
    for i in reversed(range(len(heights))):
        height= heights[i]
        minHeight = min(rightMax,maxes[i])
        if height < minHeight:
            maxes[i] = minHeight-height
        else:
            maxes[i]=0
        rightMax = max(height,rightMax)
    return sum(maxes)