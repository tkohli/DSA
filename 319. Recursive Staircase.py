def staircaseTraversal(h, maxSteps):
    if h <= 1:
		return 1
	temp = 0
	for i in range(1,min(h,maxSteps)+1):
		temp+=staircaseTraversal(h-i,maxSteps)
	return temp