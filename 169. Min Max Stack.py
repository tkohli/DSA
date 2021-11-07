# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.minMaxStack = [] # this will be a dict array storing min and max
		self.stack = []
		
    def peek(self):
    	return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
		return self.stack.pop()
	
    def push(self, number):
		newMinMax = [number,number] # Min, max
        if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[-1]
			newMinMax[0] = min(lastMinMax[0],number)
			newMinMax[1] = max(lastMinMax[1],number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

    def getMin(self):
		return self.minMaxStack[-1][0]

    def getMax(self):
        # Write your code here.
		return self.minMaxStack[-1][1]
        
