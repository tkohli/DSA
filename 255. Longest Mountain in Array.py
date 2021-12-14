"""
Find peak and the go to left and right to check its length
"""
arr = [2, 1, 4, 7, 3, 2, 5]
# arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
i = 1
while i < len(arr)-1:
    isPeak = arr[i] > arr[i+1] and arr[i] > arr[i-1]
    if not isPeak:
        i += 1
        continue
    print(arr[i])
    leftIdx = i-2
    while leftIdx >= 0 and arr[leftIdx+1] > arr[leftIdx]:
        leftIdx -= 1
        print("gg")
    rightIdx = i+2
    while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx-1]:
        rightIdx += 1
    i = rightIdx
    print(rightIdx-leftIdx-1)
