def knuthMorrisPrattAlgorithm(string, substring):
    pattern = patternSubstring(substring)
    i = j = 0
    while i < len(string):
        if string[i] == substring[j]:
            if j == len(substring)-1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1]+1
        else:
            i += 1
    return False


def patternSubstring(substring):
    pattern = [-1 for i in substring]
    i = 1
    j = 0
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i += 1
    return pattern
