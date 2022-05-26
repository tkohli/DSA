def maxSum(arr):
    rows = cols = len(arr)
    if rows < 3:
        return 0
    ans = float('-inf')
    for i in range(rows-2):
        for j in range(rows-2):
            tmp = (arr[i][j]+arr[i][j+1]+arr[i][j+2] + arr[i+1][j+1] +
                   arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if tmp > ans:
                ans = tmp
    return ans


print(maxSum([[1, 2, 3, 0, 0],
              [0, 0, 0, 0, 0],
              [2, 1, 4, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 1, 0, 1, 0]]))
