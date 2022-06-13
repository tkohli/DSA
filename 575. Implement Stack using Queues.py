# if we have to do this directly then it will look like this
from collections import deque


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]

    def empty(self) -> bool:
        if not self.empty():
            return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# for normal operations with queue we need 2 queues and
# use some clever ways


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        i = len(self.queue)
        while i > 0:
            self.queue.append(self.queue.popleft())
            i -= 1

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop()

    def top(self) -> int:
        if not self.empty():
            return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
