trips = [[4, 3, 4], [3, 2, 4], [1, 8, 9], [7, 2, 5]]
capacity = 5
start_timings = sorted([(trip[1], trip[0]) for trip in trips])
end_timings = sorted([(trip[2], trip[0]) for trip in trips])

passengers = 0
start = end = 0
while(start < len(trips)):
    if start_timings[start][0] < end_timings[end][0]:
        passengers += start_timings[start][1]
    else:
        passengers -= end_timings[end][1]
        end += 1
        continue    # watchout
    start += 1

    if passengers > capacity:
        print(False)
    # print(passengers, start_timings[start][0], end_timings[end][0])
print(True)
