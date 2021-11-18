def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    # Write your code here.
    return edits


print(levenshteinDistance("abc","yabd"))