# O(n^3) Time and O(n^2) Space
def palindromePartitioningMinCuts(string):
    palindrome = [[False for _ in range(len(string))]
                  for _ in range(len(string))]
    for i in range(len(string)):
        for j in range(i, len(string)):
            # is palindrome
            palindrome[i][j] = isPalindrome(string[i:j+1])

    cuts = [float("inf") for i in string]
    for i in range(len(cuts)):
        if palindrome[0][i]:
            cuts[i] = 0  # check for init palindrome
        else:
            cuts[i] = cuts[i-1]+1
            for j in range(1, i):
                if palindrome[j][i] and cuts[j-1]+1 < cuts[i]:
                    cuts[i] = cuts[j-1]+1
    return cuts[-1]


def isPalindrome(st):
    leftIdx = 0
    rightIdx = len(st)-1
    while leftIdx < rightIdx:
        if st[leftIdx] != st[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


#  O(n^2) Time
def palindromePartitioningMinCuts(string):
    palindrome = [[False for _ in range(len(string))]
                  for _ in range(len(string))]
    for i in range(len(string)):
        palindrome[i][i] = True
    for length in range(2,  len(string)):
        for i in range(0, len(string)-length+1):
            # is palindrome
            j = i+length-1
            if length == 2:
                palindrome[i][j] = string[i] == string[j]
            else:
                palindrome[i][j] = string[i] == string[j] and palindrome[i+1][j-1]

    cuts = [float("inf") for i in string]
    for i in range(len(cuts)):
        if palindrome[0][i]:
            cuts[i] = 0  # check for init palindrome
        else:
            cuts[i] = cuts[i-1]+1
            for j in range(1, i):
                if palindrome[j][i] and cuts[j-1]+1 < cuts[i]:
                    cuts[i] = cuts[j-1]+1
    return cuts[-1]
