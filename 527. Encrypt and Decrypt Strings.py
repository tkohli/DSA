from collections import defaultdict


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = defaultdict(int)
        self.m = {}
        for i, j in zip(keys, values):
            self.m[i] = j
        for i in dictionary:
            l = []
            for x in i:
                l.append(self.m[x])
            self.d[''.join(l)] += 1

    def encrypt(self, word1: str) -> str:
        l = []
        for x in word1:
            l.append(self.m[x])
        return "".join(l)

    def decrypt(self, word2: str) -> int:
        return self.d[word2]

        # Your Encrypter object will be instantiated and called as such:
        # obj = Encrypter(keys, values, dictionary)
        # param_1 = obj.encrypt(word1)
        # param_2 = obj.decrypt(word2)
