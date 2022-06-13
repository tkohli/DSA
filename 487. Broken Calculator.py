startValue = 2
target = 3
"""
We can only do 2 operations i.e. multiply it by 2 or sub 1
we start by 2 => 2 * 2 = 4 => 4 - 1 => 3 So we took 2 steps which is our ans 
"""
ans = 0
while startValue < target:
    ans += 1
    if target % 2 == 1:
        target += 1
    else:
        target //= 2
print(ans + startValue - target)
