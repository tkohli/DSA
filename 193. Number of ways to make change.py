def numberOfWaysToMakeChange(n, denoms):
    waysOfChange = [0 for _ in range(n+1)]
    waysOfChange[0] = 1
    for demon in denoms:
        for amount in range(1,n+1):
            if demon <= amount:
                waysOfChange[amount] += waysOfChange[amount-demon] 

    return waysOfChange[n]