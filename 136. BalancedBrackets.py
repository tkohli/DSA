# Balanced Brackets
def balanceBrackets(string):
    startingBrackets = "([{"
    closingBrackets = ')]}'
    dct = {')':'(',']':'[','}':'{'}
    stack = []
    for ch in string:
        if ch in startingBrackets:
            stack.append(ch)
        elif ch in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == dct[ch]:
                stack.pop()
            else:
                return False
    return len(stack)==0


print(balanceBrackets("({}"))