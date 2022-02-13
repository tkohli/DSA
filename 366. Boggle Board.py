def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True

    trieNode = trieNode[letter]
    if '*' in trieNode:
        finalWords[trieNode['*']] = True
    neighbors = getNeighbor(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbor(i, j, board):
    arr = []
    if i > 0 and j > 0:
        arr.append([i-1, j-1])
    if i > 0 and j < len(board[0])-1:
        arr.append([i-1, j+1])
    if i < len(board)-1 and j > 0:
        arr.append([i+1, j-1])
    if i < len(board)-1 and j < len(board[0])-1:
        arr.append([i+1, j+1])
    if i > 0:
        arr.append([i-1, j])
    if i < len(board)-1:
        arr.append([i+1, j])
    if j > 0:
        arr.append([i, j-1])
    if j < len(board[0])-1:
        arr.append([i, j+1])
        return arr


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
