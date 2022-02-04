string = '())()(()())'
stack = []
maxLen = 0
start = 0
for i, ch in enumerate(string):
    if ch == '(':
        stack.append(ch)
    else:
        if len(stack) == 0:
            maxLen = max(maxLen, i-start)
            start = i
        else:
            stack.pop()
if len(stack) == 0:
    maxLen = max(maxLen, i-start)
print(maxLen)
