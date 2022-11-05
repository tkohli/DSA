class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = Trie()
            cur = cur.children[i]
        cur.isWord = True

    def prune(self, word):
        cur = self
        nodeAndChildKey = list()
        for i in word:
            nodeAndChildKey.append((cur, i))
            cur = cur.children[i]
        for parentNode, childKey in reversed(nodeAndChildKey):
            target = parentNode.children[childKey]
            if len(target.children) == 0:
                del parentNode.children[childKey]
            else:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for i in words:
            root.addWord(i)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False
                root.prune(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")
        return list(res)
