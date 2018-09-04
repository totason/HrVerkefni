n = int(input("Enter the length of the sequence: "))
x1, x2, x3, xtemp = 0, 1, 2, 0
if n ==1:
    print(x2)
elif n == 2:
    print(x2)
    print(x3)
else:
    print(x2)
    print(x3)
    n -=2
    while 0 < n:
        xtemp = x3
        x3 = x1 + x2 + x3
        print(x3)
        x1, x2 = x2, xtemp
        n -= 1