# Element uniqueness
def unique(S, start, stop):
    if stop - start <= 1: return True
    elif not unique(S, start, stop - 1): return False
    elif not unique(S, start + 1, stop): return False
    else: return S[start] != S[stop - 1]

arr = [1, 2, 4, 4, 5]
print(unique(arr, 0, len(arr)))