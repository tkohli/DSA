def tandemBicycle(redShirtSpeeds,blueShirtSpeeds,fastest):
    """
    if fastest = true then maximum speed  else match minimum 
    """
    speed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.reverse()
    for i,j in zip(redShirtSpeeds,blueShirtSpeeds):
        speed += max(i,j)
    return speed

print(tandemBicycle([5,5,3,9,2],[3,6,7,2,1],False))
