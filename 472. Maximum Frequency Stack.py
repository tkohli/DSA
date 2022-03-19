"""
Thoughts: naive way what we can do is that start by making dct then 
keep track of all freq and manage the way while solving questions

but for bigger input it will give us TLE so let's try to keep track of freq 
and reverse our appreach i.e.
keep freq and then in it store all elements also keep track of maxFreq 
to optimize it 
"""


import collections


class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freq = {}  # store currentCount
        self.group = {}  # store list

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        f = self.freq[val]+1
        # now update the value
        self.freq[val] = f
        if f > self.maxFreq:
            self.maxFreq = f
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)
        # so that we can just pop all elements with maxFreq

    def pop(self) -> int:
        num = self.group[self.maxFreq].pop()
        self.freq[num] -= 1
        if self.group[self.maxFreq] == []:
            self.maxFreq -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


class FreqStack:

    def __init__(self):
        self.maxFeq = 0
        self.count = collections.Counter()
        self.group = collections.defaultdict(list)


    def push(self, val: int) -> None:
        f = self.count[val]+1
        self.count[val] = f
        if f>self.maxFeq:
            self.maxFeq = f
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxFeq].pop()
        self.count[x]-=1
        if self.group[self.maxFeq]==[]:
            self.maxFeq-=1
        return x

        # Your FreqStack object will be instantiated and called as such:
        # obj = FreqStack()
        # obj.push(val)
        # param_2 = obj.pop()


class FreqStack:

    def __init__(self):
        self.maxFeq = 0
        self.count = collections.Counter()
        self.group = collections.defaultdict(list)

    def push(self, val: int) -> None:
        f = self.count[val]+1
        self.count[val] = f
        if f > self.maxFeq:
            self.maxFeq = f
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxFeq].pop()
        self.count[x] -= 1
        if self.group[self.maxFeq] == []:
            self.maxFeq -= 1
        return x
