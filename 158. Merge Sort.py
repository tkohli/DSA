array = [8,5,2,9,5,6,3]

def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    leftArray = array[:mid]
    rightArray = array[mid:]
    return mergeSortedArray(mergeSort(leftArray),mergeSort(rightArray))

def mergeSortedArray(arrayOne,arrayTwo):
    i,j =0,0
    out = []
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] < arrayTwo[j]:
            out.append(arrayOne[i])
            i+=1
        else:
            out.append(arrayTwo[j])
            j+=1
    while i < len(arrayOne):
        out.append(arrayOne[i])
        i+=1
    while j < len(arrayTwo):
        out.append(arrayTwo[j])
        j+=1
    return out

print(mergeSort(array))
