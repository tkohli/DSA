# Minimum Speed to Arrive on Time

dist = [1,3,2]
hour = 2.7


def isPossible( dist, speed, hour):
    ans = 0
    for i in range(len(dist)):
        d = dist[i] * 1.0 / speed
        if i != len(dist) - 1:
            ans = ans + math.ceil(d)
        else:
            ans += d
        if ans > hour:
            return False
    return ans <= hour

def minSpeedOnTime(dist, hour) :
    i, j = 1, int(1e7)
    min_speed = -1
    while i <= j:
        mid = i + (j - i) // 2
        if self.isPossible(dist, mid, hour):
            min_speed = mid
            j = mid - 1
        else:
            i = mid + 1
    return min_speed


print(minSpeedOnTime(dist, hour))
