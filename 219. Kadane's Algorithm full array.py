def kadanesAlgorithm(array):
    start = 0
    end = 0
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for i in range(1,len(array)):
        num = array[i]
        maxEndingHere = max(num,maxEndingHere+num)
        if maxEndingHere==num:
            start = i
        maxSoFar = max(maxSoFar,maxEndingHere)
        if maxSoFar==maxEndingHere:
            end = i
    return array[start:end+1],maxSoFar

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
