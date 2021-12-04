def sunsetViews(buildings, direction):
    view = []
    startIdx = 0 if direction=="EAST" else len(buildings)-1
    step = 1 if direction=="EAST" else -1
    idx = startIdx
    while idx>=0 and idx<len(buildings):
        buildingHeight = buildings[idx]
        while len(view)>0 and buildings[view[-1]]<=buildings[idx]:
            view.pop()
        view.append(idx)
		idx+=step
    return view if direction=="EAST" else view[::-1]
