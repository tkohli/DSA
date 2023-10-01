# Reverse Words in a String III

s = "Let's take LeetCode contest"


def reverseWords(s) :
    ans = []
    s2 = s.split(" ")
    # print(s2)
    for word in s2:
        ans.append(word[::-1])
    # print(ans)
    return " ".join(ans)

print(reverseWords(s))
