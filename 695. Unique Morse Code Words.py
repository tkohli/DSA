class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sign = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ans = set()
        for word in words:
            tmp = ""
            for ch in word:
                tmp += (sign[ord(ch)-ord("a")])
            # tmp+=
            ans.add(tmp)
        return len(ans)
