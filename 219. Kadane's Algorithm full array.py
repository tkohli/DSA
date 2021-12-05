def kadanesAlgorithm(array):
    start = 0
    end = 0
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for i in range(1,len(array)):
        num = array[i]
        if maxEndingHere+num>num:
            maxEndingHere+=num
            end=i
        else:
            start = i
            maxEndingHere = num

        # maxEndingHere = max(num,maxEndingHere+num)
        if maxSoFar<maxEndingHere:
            maxSoFar = maxEndingHere
            end=i
        # maxSoFar = max(maxSoFar,maxEndingHere)
    return array[start:end-1],maxSoFar

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
