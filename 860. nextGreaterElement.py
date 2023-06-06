"""
arr = [2, 5,-3,-4, 6, 7, 2]
O/P = [5, 6, 6, 6, 7,-1, 5]

Approach 1 left to right NOTE use index :)
We start with                                                   stack = []     ans = [-1,-1,-1,-1,-1,-1,-1]
we get bigger value we pop
we get smaller we append
when we see 
We append                                                       stack = [2]    ans = [-1,-1,-1,-1,-1,-1,-1]     
since 5>2 so we pop it (using while loop) and append 5 to it    stack = [5]    ans = [5,-1,-1,-1,-1,-1,-1]
now 5>-3 so we append it                                        stack = [5,-3]    ans = [5,-1,-1,-1,-1,-1,-1]
now -3>-4 so we append it                                       stack = [5,-3,-4]    ans = [5,-1,-1,-1,-1,-1,-1]
now we have 6 >-4 so we pop it using while loop                 stack = [6]    ans = [5,6,6,6,-1,-1,-1]
now 7>6                                                         stack = [7]    ans = [5,6,6,6,7,-1,-1]
now 7>2 then we add it in stack                                 stack = [7,2]    ans = [5,6,6,6,7,-1,-1]
then rotate in array to find 5 so we pop 2 from array then      stack = [7]    ans = [5,6,6,6,7,-1,5]
"""
def nextGreaterElement(arr):
    res = [-1]*len(arr)
    stack = []
    for i in range(len(arr)*2):
        cirIdx = i%len(arr)
        while len(stack) and arr[stack[-1]] < arr[cirIdx]:
            top = stack.pop()
            res[top] = arr[cirIdx]
        stack.append(cirIdx)
    return res
print(nextGreaterElement([2, 5,-3,-4, 6, 7, 2]))

"""
arr = [2, 5,-3,-4, 6, 7, 2]
O/P = [5, 6, 6, 6, 7,-1, 5]

Approach 2 right to left and use values :) 
We start with                                                   stack = []     ans = [-1,-1,-1,-1,-1,-1,-1]
cur = 2 do nothin 
cur = 7                                                         stack = [7]     ans = [-1,-1,-1,-1,-1,-1,-1]
CUR = 6  SINCE 7>6                                              stack = [7,6]   ans = [-1,-1,-1,-1, 7,-1,-1]        
cur = -4                                                        stack = [7,6,-4]   ans = [-1,-1,-1, 6, 7,-1,-1]        
cur = -3                                                        stack = [7,6]   ans = [-1,-1, 6, 6, 7,-1,-1]        
cur = 5                                                         stack = [7,6,5]   ans = [-1, 6, 6, 6, 7,-1,-1]        
cur = 2                                                         stack = [7,6,5,2]   ans = [5, 6, 6, 6, 7,-1,-1]        
loop again and update the rest of value smililarly                                                                                                                
"""
def nextGreaterElement2(arr):
    res = [-1]*len(arr)
    stack = []
    for i in range((len(arr)*2)-1,-1,-1):
        cirIdx = i%len(arr)
        while stack:
            if stack[-1]<=arr[cirIdx]:
                stack.pop()
            else:
                res[cirIdx] = stack[-1]
                break
        stack.append(arr[cirIdx])
    return res

print(nextGreaterElement2([2, 5,-3,-4, 6, 7, 2]))
