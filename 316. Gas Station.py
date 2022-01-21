def validStartingCity(cost, gas, mpg):
    gas_tank, start_index = 0, 0

    for i in range(len(gas)):
        gas_tank += gas[i]*mpg - cost[i]

        if gas_tank < 0:
            start_index = i+1
            gas_tank = 0

    return start_index
