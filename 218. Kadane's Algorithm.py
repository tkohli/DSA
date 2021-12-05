def kadanesAlgorithm(array):
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for num in array[1:]:
        maxEndingHere = max(num,maxEndingHere+num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar
