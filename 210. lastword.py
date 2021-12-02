class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        currentLen = 0
        out = 0
        for s in reversed(A):
            if s.isalpha():
                currentLen+=1
            elif currentLen == 0 and s == " ":
                continue
            else:
                return currentLen
        return currentLen
        #     if s.isalpha():
        #         currentLen+=1
                
        #     elif s == ' ':
        #         out = currentLen
        #         currentLen=0
        # return out