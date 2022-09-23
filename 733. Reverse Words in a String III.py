class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split())

        # res = ''
        # l, r = 0, 0
        # while r < len(s):
        #     if s[r] != ' ':
        #         r += 1
        #     elif s[r] == ' ':
        #         res += s[l:r + 1][::-1]
        #         r += 1
        #         l = r
        # res += ' '
        # res += s[l:r + 2][::-1]
        # return res[1:]
