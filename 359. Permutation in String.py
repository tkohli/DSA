class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # map of charactar to an index in range a-z.
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')
            s1count[index] = s1count[index] + 1
            s2count[index2] = s2count[index2] + 1

        # count how many characters matches are initially set by looking at the first len(s1)
        # characters of s1 and s2.
        matches = 0
        for index in range(26):  # transverse each character.
            if s1count[index] == s2count[index]:
                matches = matches + 1

        # traverse a fixed window in s2, starting from the left
        # adding a character at a time on the right
        # and removing a character on the left
        left = 0
        # start after initial window sized to len(s1)
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # update indexes for character that was added on right
            index = ord(s2[right]) - ord('a')
            s2count[index] = s2count[index] + 1  # update character for s
            if s1count[index] == s2count[index]:
                # now they are equal
                matches = matches + 1
            elif s1count[index] + 1 == s2count[index]:
                # they were equal, but now they are not equal anymore
                matches = matches - 1

            # update indexes for character that was added on left
            index = ord(s2[left]) - ord('a')
            s2count[index] = s2count[index] - 1
            if s1count[index] == s2count[index]:
                matches = matches + 1
            elif s1count[index] - 1 == s2count[index]:
                matches = matches - 1

            # update left window
            left = left + 1

        return matches == 26
