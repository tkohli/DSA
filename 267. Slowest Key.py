releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
maxDuration = releaseTimes[0]
prev = maxDuration
idx = 0
for i, time in zip(range(0, len(releaseTimes)), releaseTimes[1:]):
    if maxDuration <= (time-prev) and keysPressed[i] < keysPressed[idx]:
        idx = i
        maxDuration = time-prev
    prev = time
print(keysPressed[i])
