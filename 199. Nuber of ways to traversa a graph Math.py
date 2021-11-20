def numberOfWaysToTraverseGraph(width, height):
    num = 1
    den = 1
    for n in range(width+height-2,max(width,height)-1,-1):
        num*=n
    for d in range(min(width,height)-1,0,-1):
        den*=d
    return num//den
print(numberOfWaysToTraverseGraph(4,3))
