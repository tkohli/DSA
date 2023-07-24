# Pow(x, n)

x = 2.00000, n = 10

def myPow(self, x, n):
    if n==0:
        return 1
    if n<0:
        return 1/(self.myPow(x,-n))
    if n % 2:
        return x * self.myPow(x, n-1)
    return self.myPow(x*x, n/2)



print(myPow(self, x, n))
