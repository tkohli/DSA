# Peak Index in a Mountain Array

arr = [0,10,5,2]

def peakIndexInMountainArray(arr):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l

print(peakIndexInMountainArray(arr))
