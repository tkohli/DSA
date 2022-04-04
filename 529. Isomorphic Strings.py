class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []
        s = list(s)
        for ch in s:
            if ch in "aeiouAEIOU":
                vowel.append(ch)
        i = len(vowel) - 1
        for j, ch in enumerate(s):
            if i < 0:
                return "".join(s)
            if ch in "aeiouAEIOU":
                s[j] = vowel[i]
                i -= 1
        return "".join(s)
