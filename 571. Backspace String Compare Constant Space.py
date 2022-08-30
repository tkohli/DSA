class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # I am gonna use stack
        s1 = []
        for ch in s:
            if ch == '#':
                if len(s1) == 0:
                    continue
                s1.pop()
            else:
                s1.append(ch)
        s2 = []
        for ch in t:
            if ch == '#':
                if len(s2) == 0:
                    continue
                s2.pop()
            else:
                s2.append(ch)

        return s1 == s2
