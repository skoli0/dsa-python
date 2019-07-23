# Linear sum for n items

arr = [2, 4, 3, 6, 9, 15, 1, 5]
arr = [4, 3, 6, 2, 8]
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]

print(linear_sum(arr, 3))