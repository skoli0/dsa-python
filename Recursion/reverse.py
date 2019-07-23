def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)

arr = list(range(1, 11))
print(arr)
reverse(arr, 0, len(arr))
print(arr)