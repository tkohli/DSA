def groupAnagrams(words):
    dict = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in dict:
            dict[sortedWord].append(word)
        else:
            dict[sortedWord] = [word]
    return list(dict.values())
