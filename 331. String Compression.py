class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 1
        encoding = []
        for i in range(len(chars)-1, -1, -1):
            if i and chars[i] == chars[i-1]:
                chars.pop(i)
                l += 1
            else:
                if l > 1:
                    for s in str(l)[::-1]:
                        chars.insert(i+1, s)
                    l = 1
        return len(chars)
