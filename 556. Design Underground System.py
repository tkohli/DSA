from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.user = defaultdict(list)
        self.dest = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, prevTime = self.user[id]
        self.dest[(startStation, stationName)].append(t-prevTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(sum(self.dest[(startStation, endStation)]))/len(self.dest[(startStation, endStation)])

        # Your UndergroundSystem object will be instantiated and called as such:
        # obj = UndergroundSystem()
        # obj.checkIn(id,stationName,t)
        # obj.checkOut(id,stationName,t)
        # param_3 = obj.getAverageTime(startStation,endStation)
