# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.lower = Heap(MAX_HEAP_FUNC, [])
        self.greater = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    def insert(self, number):
        if not self.lower.length or number < self.lower.peek():
            self.lower.insert(number)  # start me insert
        else:
            self.greater.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lower.length - self.greater.length == 2:
            self.greater.insert(self.lower.remove())
        if self.greater.length - self.lower.length == 2:
            self.lower.insert(self.greater.remove())

    def updateMedian(self):
        if self.lower.length == self.greater.length:
            self.median = (self.lower.peek()+self.greater.peek())/2
        elif self.lower.length > self.greater.length:
            self.median = self.lower.peek()
        else:
            self.median = self.greater.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparisonFun, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.comparisonFun = comparisonFun
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx*2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx*2+2 if currentIdx*2+2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFun(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx

            if self.comparisonFun(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx*2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2
        while currentIdx > 0:
            if self.comparisonFun(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx-1)//2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b
