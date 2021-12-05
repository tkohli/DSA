def kadanesAlgorithm(array):
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for num in array[:]:
        maxEndingHere = max(maxEndingHere,maxEndingHere+num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar
