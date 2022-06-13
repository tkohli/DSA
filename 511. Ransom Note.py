class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st = ransomNote
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for ch in st:
            if ransomNote[ch] > magazine[ch]:
                return False
        return True
