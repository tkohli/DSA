class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        lst = []
        for k, v in cnt.items():
            lst.append([k, v])
        lst.sort(key=lambda x: -x[1])
        s = ""
        for item in lst:
            s += (item[0]*item[1])
        return s

# we can use bucket sort to optimize time :)
