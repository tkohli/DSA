"""
 FYI 
 West   East
  <-     ->
buildings = [3,5,4,4,3,1,3,2]
direction = "EAST"
  |
  | | |
| | | | |   | 
| | | | |   | |
| | | | | | | |
0 1 2 3 4 5 6 7

OP = [1,3,6,7]
"""


def sunsetViews(buildings, direction):
    view = []
    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1
    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]
        while len(view) > 0 and buildings[view[-1]] <= buildingHeight:
            view.pop()
        view.append(idx)
        idx += step
    return view if direction == "EAST" else view[::-1]
