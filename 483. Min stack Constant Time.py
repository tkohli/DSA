class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []

    def push(self, val: int) -> None:
        if self.minst != []:
            if self.minst[-1] > val:
                self.minst.append(val)
            else:
                self.minst.append(self.minst[-1])
        else:
            self.minst.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.minst.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
