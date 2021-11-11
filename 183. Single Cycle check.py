def hasSingleCycle(array):
	n = 0
	currentIdx = 0
	while n < len(array):
		if n > 0 and currentIdx == 0:
			return False
		n+=1
		currentIdx = (currentIdx+array[currentIdx])%len(array)
		if currentIdx<0:
			currentIdx += len(array)
	return currentIdx == 0
