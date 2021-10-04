# nonConstructibleChange
def nonConstructibleChange(coins):
    coins.sort()
    currentSum = 0
    for coin in coins:
	    if coin > currentSum +1 :
		    return currentSum +1 
        currentSum +=coin 
    return currentSum +1 
