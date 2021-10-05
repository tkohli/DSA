def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	current = float("inf")
	smallest = float("inf")
	idxOne = 0
	idxTwo = 0
	smallestList = []
	while idxOne<len(arrayOne) and idxTwo<len(arrayTwo):
		First = arrayOne[idxOne]
		Second = arrayTwo[idxTwo]
		if First > Second:
			current = First - Second
			idxTwo +=1
		elif First < Second:
			current = Second - First 
			idxOne +=1
		else:
			return [First,Second]
		if current < smallest:
			smallest =  current
			smallestList = [First,Second]
	return smallestList
			