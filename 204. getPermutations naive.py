# O(n*n*n!) Time and O(n*n!) Space 
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutations, permutations):
    if not len(array) and len(currentPermutations):
        permutations.append(currentPermutations)
    else:
        for i in range(len(array)):
            newArray = array[:i]+array[i+1:]
            newPermutations = currentPermutations+[array[i]]
            permutationsHelper(newArray,newPermutations,permutations)
    
print(getPermutations([1,2,3]))