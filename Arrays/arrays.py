arr = [1, 2, 3, 4, 5]

for i in arr:
    print(i)

print('\n')
for i in range(len((arr))):
    print(arr[i])

index = 2
print('element at index {} is {}'.format(index, arr[index]))

print(arr[:])

# find max
_max = arr[0]
for i in range(len(arr)):
    if arr[i] > _max:
        _max = arr[i]
print('maxium of array {}'.format(_max))

_min = arr[0]
for i in range(len(arr)):
    if arr[i] < _min:
        _min = arr[i]

print('minimum of array {}'.format(_min))