from random import randrange
from turtle import st


def underscorifySubstring(string, substring):
    location = collapse(getLocation(string, substring))
    temp = 0
    print(location)
    string = list(string)
    for i in range(len(location)):
        string.insert(location[i][0]+temp, '_')
        temp += 1
        string.insert(location[i][1]+temp, '_')
        temp += 1
    print("".join(string))


def getLocation(string, subString):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        if subString == string[startIdx:startIdx+len(subString)]:
            locations.append([startIdx, startIdx+len(subString)])
            startIdx += 1
        else:
            startIdx += 1
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    prev = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= prev[1]:
            prev[1] = current[1]
        else:
            newLocations.append(current)
            prev = current
    return newLocations


underscorifySubstring(
    "testthis is a testtest to see if testestest it works", 'test')
