# O(n) Time complexity | O(n) Space Complexity
def nextGreaterElement(array):
    result = [-1 for _ in range(len(array))]
    stack = []
    for idx in range(2*len(array)-1,-1,-1):
        cirIdx = idx % len(array)
        while len(stack) > 0:
            if stack[-1] <= array[cirIdx]:
                stack.pop()
            else:
                result[cirIdx] = stack[len(stack)-1]
				break
        stack.append(array[cirIdx])
    return result
