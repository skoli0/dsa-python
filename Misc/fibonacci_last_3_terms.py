def fib_last3(n):
    a, b, c = 0, 0, 1
    print(a, b, c, end = ' ')
    for i in range(4, n + 1):
        # print(a, b, c, end = ' ')
        a, b, c = b, c, a + b + c
        # print(a, b, c)

fib_last3(5)