# Make The String Great

class Solution:
    def makeGood(self, string: str) -> str:
        stack = [string[0]]

        for i in range(1, len(string)):
            if len(stack) == 0:
                stack.append(string[i])
                continue
            if abs(ord(stack[-1]) - ord(string[i])) == 32:
                stack.pop()
            else:
                stack.append(string[i])
                
        return("".join(stack))
