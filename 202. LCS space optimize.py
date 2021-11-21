# In this we optimize te space
def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1)<len(str2) else str2
    big = str1 if len(str1)>=len(str2) else str2
    even = [[] for x in range(len(small)+1)]
    odd = [[] for x in range(len(small)+1)]
    for i in range(1,len(big)+1):
        if i%2==1:
            current= odd
            prev = even
        else:
            current = even
            prev = odd
        for j in range(1,len(small)+1):
            if big[i-1]==small[j-1]:
                current[j] = prev[j-1]+[big[i-1]]
            else:
                current[j] = max(prev[j],current[j-1],key=len)
    return even[-1] if len(big)%2==0 else odd[-1]