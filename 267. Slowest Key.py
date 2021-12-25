class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        maxTime = releaseTimes[0]
        currentTime, currentKey = 0, 0
        for i in range(len(keysPressed)-1):
            j = i+1
            currentTime = releaseTimes[j]-releaseTimes[i]
            if currentTime > maxTime:
                maxTime = currentTime
                currentKey = j
            elif currentTime == maxTime and (keysPressed[j]) > (keysPressed[currentKey]):
                currentKey = j
        return (keysPressed[currentKey])
