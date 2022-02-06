class Bitset:

    def __init__(self, size: int):

        self.string = [0]*size
        self.flipp = [1]*size
        self.ones = 0
        self.size = size

    def fix(self, idx: int) -> None:

        if self.string[idx] == 0:
            self.ones += 1

        self.string[idx] = 1
        self.flipp[idx] = 0

    def unfix(self, idx: int) -> None:

        if self.string[idx] == 1:
            self.ones -= 1

        self.string[idx] = 0
        self.flipp[idx] = 1

    def flip(self) -> None:

        self.string, self.flipp = self.flipp, self.string

        # if you use this line instead of above line then it will give you the TLE

        # self.string,self.flipp=self.flipp[::],self.string[::]

        #####################

        self.ones = self.size - self.ones

    def all(self) -> bool:

        return self.ones == self.size

    def one(self) -> bool:

        return self.ones > 0

    def count(self) -> int:

        return self.ones

    def toString(self) -> str:

        return "".join(map(str, self.string))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
