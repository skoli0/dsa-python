def largestRange(array):
    lstRage = []
    longestLength = 0
    numbers = {}
    for num in array:
        numbers[num] = True
#     print(numbers)
    for num in array:
        if not numbers[num]:
            continue
        numbers[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in numbers:
            numbers[left] = False
            currentLength += 1
            left -= 1
        while right in numbers:
            numbers[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            lstRage = [left + 1, right - 1]
    return lstRage

a = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
a = [2, 3, 4, 5, 6]
print(largestRange(a))
