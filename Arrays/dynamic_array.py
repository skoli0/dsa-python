import ctypes

class DynamicArray:
    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._create_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('Invalid index.')

        return self._A[k]

    def append(self, obj):
        """Add an object at end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if not self._n >= 0:
            raise IndentationError('Array is empty')
        
        _popped = self._A[0]
        for i in range(1, self._n):
            self._A[i - 1] = self._A[i]
        self._A[self._n - 1] = None
        self._n -= 1

        return _popped

    def remove_at(self, k):
        """Remove element from given index."""
        _removed = self._A[k]

        for i in range(k + 1, self._n):
            self._A[i - 1] = self._A[i]
        self._A[self._n - 1] = None
        self._n -= 1

        return _removed


    def _resize(self, c):
        """Resize internal array with capacity c."""
        B = self._create_array(c)
        for k in range(self._n):
            B[k] = self._A[k]

        self._A = B
        self._capacity = c

    def _create_array(self, c):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()

da = DynamicArray()
print(len(da))
print(da._capacity)
da.append(10)
da.append(20)
print(da._capacity)
da.append(30)
da.append(40)
print(da._capacity)
da.append(50)

print(da._capacity)
for i in da:
    print(i)
print(len(da))
print(da.pop())
print(len(da), da._capacity)

print('\n')
for i in da:
    print(i)

da.append(60)
da.append(70)
da.append(80)
da.append(90)
da.append(100)
da.remove_at(4)
da.remove_at(4)
da.remove_at(1)
da.remove_at(1)
da.remove_at(0)
print(len(da), da._capacity)

print('\n')
for i in da:
    print(i, end=' ')
print('\n', len(da), da._capacity)
# import array

# s = array.array('i', [10, 20, 30])
# for i in s:
#     print(type(i))