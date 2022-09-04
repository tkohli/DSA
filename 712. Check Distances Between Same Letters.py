class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dct = defaultdict(list)
        for i, ch in enumerate(s):
            dct[ch].append(i)
        for k, v in dct.items():
            for i in range(1, len(v)):
                if v[i]-v[i-1]-1 != distance[ord(k)-97]:
                    print(ord(k)-97, distance[ord(k)-97])
                    return False
        return True
