def longestCommonSubsequence(str1, str2):
    lcs = [[[None,0,None,None]for x in range(len(str1)+1)]for y in range(len(str2))]
    # First None if char is not used else store None
    # 0 to check current length
    # next 2 none having I and J 
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                pass
