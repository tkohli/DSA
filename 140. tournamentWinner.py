# tournamentWinner
def tournamentWinner(competitions, results):
	dct = {}
    for comp in competitions:
        if comp[0] not in dct:
            dct[comp[0]] = 0
        if comp[1] not in dct:
            dct[comp[1]] = 0

    for comp,result in zip(competitions,results):
        if result:
            dct[comp[0]] += 1
        else:
            dct[comp[1]] += 1
    print(dct)
    Keymax = max(zip(dct.values(), dct.keys()))
    return (Keymax[1])
