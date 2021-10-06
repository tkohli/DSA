def arrayOfProducts(array):
	products = []
	for i in range(len(array)):
		runningProducts = 1
		for j in range(len(array)):
			if i != j:
				runningProducts*=array[j]
		products.append(runningProducts)
		
	return products
	