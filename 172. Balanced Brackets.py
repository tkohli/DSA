def balancedBrackets(string):
    startingBrackets = '([{'
	endingBrackets = ')]}'
	dict = {')':'(',']':'[','}':'{'}
	stack = []
	for s in string:
		if s in startingBrackets:
			stack.append(s)
		elif s in endingBrackets:
			if len(stack) == 0:
				return False
			if  stack[-1] == dict[s]:
				stack.pop()
			else:
				return False
	return len(stack) == 0

