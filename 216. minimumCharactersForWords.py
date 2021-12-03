# O(c) Time complexity | O(n*l) Space complexity
def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}

    for word in words:
        charFreq = countCharFreq(word)
        updateMaxFeq(charFreq,maximumCharacterFrequencies)
    return makeArray(maximumCharacterFrequencies)

def countCharFreq(string):
    charFreq = {}
    for ch in string:
        if ch not in charFreq:
            charFreq[ch]=0
        charFreq[ch]+=1
    return charFreq


def updateMaxFeq(freq,maxFreq):
    for ch in freq:
        fre = freq[ch]
        if ch in maxFreq:
            maxFreq[ch] = max(fre,maxFreq[ch])
        else:
            maxFreq[ch] = fre


def makeArray(Freq):
    char = []
    for ch in Freq:
        fre = Freq[ch]
        for _ in range(fre):
            char.append(ch)
    return char