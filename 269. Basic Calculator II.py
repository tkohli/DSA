# We can implement idt using stack
s = "3+2*2"
s = ("".join(s.split())).reversed()
print(s)
ans = 0
num = ''
for n in s:
    if n.isdigit():
        num += n
    elif n == "+":
        ans = ans+int(num)
        num = ''
    elif n == "-":
        ans = ans-int(num)
        num = ''
    elif n == "*":
        ans = ans*int(num)
        num = ''
    elif n == "/":
        ans = ans/int(num)
        num = ''

print(ans)
