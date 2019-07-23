# 1, 1, 2, 3, 5, 8
def bad_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)
    
print(bad_fibonacci(5))

def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        a, b = good_fibonacci(n - 1)
        return (a + b, a)

print(good_fibonacci(9)[0])