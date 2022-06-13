class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # a placeholder to mark stack is empty. This eliminates the need to do an empty check later
        stck = [['$', 0]]
        for c in s:
            if stck[-1][0] == c:
                # update occurences count of top element if it matches current character
                stck[-1][1] += 1
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])
        return ''.join(c * cnt for c, cnt in stck)
