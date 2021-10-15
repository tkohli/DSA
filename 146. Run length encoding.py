def runLengthEncoding(string):
	out = []
	currentLength = 1
	for i in range(1,len(string)):
		prevChar = string[i-1]
		currentChar = string[i]

		if prevChar != currentChar or currentLength == 9:
			out.append(str(currentLength))
			out.append(prevChar)
			currentLength = 0
		currentLength+=1
	# for last value
	out.append(str(currentLength))
	out.append(string[-1])
	return ("".join(out))  
    
