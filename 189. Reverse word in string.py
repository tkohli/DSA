def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord]== ' ':
            words.append(" ")
            startOfWord = idx
    words.append(string[startOfWord:])
    left = 0
    right = len(words)-1
    while left<right:
        words[left],words[right]=words[right],words[left]
        left +=1
        right -=1
    return "".join(words)
print(reverseWordsInString("AlgoExpert is the best"))