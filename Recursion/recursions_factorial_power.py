def power(num, pwr):
    if pwr == 1:
        return 1
    else:
        return num * power(num, pwr - 1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def recursive_fibonacci(num):
    if num <= 1:
        return (0, num)
    else:
        a, b = recursive_fibonacci(num - 1)
        print(a, end=' ')
        return (a + b, a)

def iterative_fibonacci(num):
    
    a, b = 0, 1
    print(a, end=' ')
    for i in range(2, num):
        a, b = a + b, a
        print(a, end=' ')


print(power(2, 3))
print(factorial(5))
print('\nrecursive fibonnaci: ', recursive_fibonacci(10))
iterative_fibonacci(10)