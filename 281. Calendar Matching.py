def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # add time from 00:00 to 23.59
    cal1 = updateCalender(calendar1, dailyBounds1)
    cal2 = updateCalender(calendar2, dailyBounds2)
    # now merge calenders
    mergedCal = mergedCalenders(cal1, cal2)
    # join overlapping interval or flatten it up
    flattenCal = flatten(mergedCal)
    # find availability
    return getMatching(flattenCal, meetingDuration)


def updateCalender(calender, DailyBounds):
    updatedCalender = calender[:]
    updatedCalender.insert(0, ["0:00", DailyBounds[0]])
    updatedCalender.append([DailyBounds[1], "23:59"])
    return list(map(lambda m: [timeToMins(m[0]), timeToMins(m[1])], updatedCalender))


def mergedCalenders(cal1, cal2):
    merged = []
    i, j = 0, 0
    while i < len(cal1) and j < len(cal2):
        meet1, meet2 = cal1[i], cal2[j]
        if meet1[0] < meet2[0]:
            merged.append(meet1)
            i += 1
        else:
            merged.append(meet2)
            j += 1
    while i < len(cal1):
        merged.append(cal1[i])
        i += 1
    while j < len(cal2):
        merged.append(cal2[j])
        j += 1
    return merged


def flatten(cal):
    flattened = [cal[0][:]]
    for i in range(1, len(cal)):
        current = cal[i]
        prev = flattened[-1]
        currentStart, currentEnd = current
        prevStart, prevEnd = prev
        if prevEnd >= currentStart:
            newPrevMeeting = [prevStart, max(prevEnd, currentEnd)]
            flattened[-1] = newPrevMeeting
        else:
            flattened.append(current[:])
    return flattened


def getMatching(cal, meetingDuration):
    matching = []
    for i in range(1, len(cal)):
        start = cal[i-1][1]
        end = cal[i][0]
        avail = end-start
        if avail >= meetingDuration:
            matching.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matching))


def timeToMins(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours*60 + minutes


def minutesToTime(minutes):
    hour = str(minutes//60)
    minutes = minutes % 60
    minutes = "0"+str(minutes) if minutes < 10 else str(minutes)
    return hour+":"+minutes
