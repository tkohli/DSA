def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1
    # Write your code here.
    return numberOfWaysToTraverseGraph(width-1,height) + numberOfWaysToTraverseGraph(width,height-1)
