n = int(input("Enter the length of the sequence: "))
x1 = 0
x2 = 1
x3 = 2
xtemp = 0
if n ==1:
    print(x2)
elif n == 2:
    print(x2, x3)
else:
    print(x2, x3, end =' ')
    while 0 < n:
        xtemp = x3
        x3 = x1 + x2 + x3
        print(x3, end = ' ')
        x1 = x2
        x2 = xtemp
        n -= 1