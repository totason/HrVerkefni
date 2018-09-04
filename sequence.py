n = int(input("Enter the length of the sequence: "))
x1 = 1
x2 = 2
x3 = 0
xtemp = 0
if n ==1:
    print(x1)
elif n == 2:
    print(x1, x2)
else:
    print(x1, x2, end =',')
while 0 < n:
    xtemp = x3
    x3 = x1 + x2 + x3
    print(x3, end = ',')
    x1 = x2
    x2 = xtemp
    n -= 1