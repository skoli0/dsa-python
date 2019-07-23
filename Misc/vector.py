class Vector:
    """Represent a vector in mulidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val
    
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has some coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other    # rely on existing __eq__ definition

    def __str__(self):
        """Produce string represention of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main':    
    v1 = Vector(3)
    print(str(v1))
    print(len(v1))
    for i in range(0, len(v1)):
        v1[i] = i + 11

    print(str(v1))

    v2 = Vector(3)
    print(str(v2))
    print(len(v2))
    for i in range(0, len(v2)):
        v2[i] = i + 1

    print(str(v2))

    print(v1 + v2)
    print(v1 == v2)
    print(v1 != v2)