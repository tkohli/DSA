# Find the Difference


s = "abcd"
t = "abcde"

def findTheDifference(s,t):
    t1 = 0
    for i in s:
        t1+=ord(i)

    t2 = 0
    for j in t:
        t2+=ord(j)
    
    return chr(t2-t1)

print(findTheDifference(s,t))
