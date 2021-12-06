# O(n*2^n) Time  complexity | O((n*2^n)) Space complexity
def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            current = subsets[i]
            subsets.append(current+[ele])

    return subsets

print(powerset([1,2,3]))