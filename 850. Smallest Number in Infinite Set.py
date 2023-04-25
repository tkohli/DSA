# Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cur = 1
        self.seen = set()

    def popSmallest(self) -> int:
        if self.heap:
            tmp = heappop(self.heap)
            self.seen.remove(tmp)
            return tmp
        n = self.cur
        self.cur+=1
        return n

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.seen: # 10<4
            heappush(self.heap,num)
            self.seen.add(num)

# seen - constant search
# heap [1]
# cur = 4

# 4-1000
            


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# maintain a variable which points to the current smallest element untill addBack is called
# when addBack() is called only add elements to the set which were popped earlier i.e. smaller than cur
# when popSmallest() is called return the top most element in the set if it exists else return cur


