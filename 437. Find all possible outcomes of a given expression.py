
# Python3 program to evaluate all
# possible values of a expression
 
# Utility function to evaluate a simple
# expression with one operator only.
def eval(a, op, b):
 
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
 
# This function evaluates all possible values
# and returns a list of evaluated values.
def evaluateAll(expr, low, high):
 
    # To store result (all possible
    # evaluations of given expression 'expr')
    res = []
 
    # If there is only one character,
    # it must be a digit (or operand),
    # return it.
    if low == high:
     
        res.append(int(expr[low]))
        return res
 
    # If there are only three characters,
    # middle one must be operator and 
    # corner ones must be operand
    if low == (high - 2):
     
        num = eval(int(expr[low]),
                       expr[low + 1],
                   int(expr[low + 2]))
 
        res.append(num)
        return res
 
    # every i refers to an operator
    for i in range(low + 1, high + 1, 2):
     
        # l refers to all the possible values
        # in the left of operator 'expr[i]'
        l = evaluateAll(expr, low, i - 1)
 
        # r refers to all the possible values
        # in the right of operator 'expr[i]'
        r = evaluateAll(expr, i + 1, high)
 
        # Take above evaluated all possible
        # values in left side of 'i'
        for s1 in range(0, len(l)):
         
            # Take above evaluated all possible
            # values in right side of 'i'
            for s2 in range(0, len(r)):
             
                # Calculate value for every pair
                # and add the value to result.
                val = eval(l[s1], expr[i], r[s2])
                res.append(val)
     
    return res
 
# Driver Code
if __name__ == "__main__":
 
    expr = "1*2+3*4"
    length = len(expr)
    ans = evaluateAll(expr, 0, length - 1)
 
    for i in range(0, len(ans)):
        print(ans[i])