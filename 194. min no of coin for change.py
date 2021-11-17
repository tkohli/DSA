def minNumberOfCoinsForChange(n, denoms):# n is money
    minChange = [float('inf') for amount in range(n+1)]
    minChange[0] = 0
    for denom in denoms:
        for i in range(len(minChange)):
            if denom>=i:
                minChange[i]=min(minChange[i],minChange[i-denom]+1)
    return minChange[n] if minChange[n] != float("inf") else -1