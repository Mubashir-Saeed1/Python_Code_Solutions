import ctypes


class DynamicArrays:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self._createarray(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if 0 > item >= self.capacity:
            return ValueError('Out of Range'), IndexError('Index Range out of Bounds')
        return self.A[item]

    def append(self, element):
        if self.capacity == self.n:
            self._resize(2 * self.capacity)
        self.A[self.n] = element
        self.n += 1

    def inarray(self, element):
        yes = False
        for x in range(self.n):
            if self.A[x] == element:
                yes = True
                break
        if yes:
            print(f'{element} is in the Array')
        else:
            print(f'{element} is not in the Array!')

    def insert(self, ind, element):
        insertable = self._createarray(self.capacity)
        for x in range(self.n):
            print(f'Printed: {x}')
            if x == ind:
                insertable[x] = element
            else:
                insertable[x] = self.A[x]
        self.A = insertable
        self.n += 1

    def remove(self, element):
        array = self._createarray(self.capacity)
        for x in range(self.n):
            if self.A[x] != element:
                array[x] = self.A[x]
        self.n -= 1
        self.A = array

    def _resize(self, oldcap):
        b = self._createarray(oldcap)
        for k in range(self.n):
            b[k] = self.A[k]
        self.A = b
        self.capacity = oldcap

    def _createarray(self, cap):
        return (cap * ctypes.py_object)()


arr = DynamicArrays()
arr.append(4)
arr.append(5)
arr.append(6)
arr.append(7)
print(arr[0])
arr.append(20)
print(arr[1])
print(len(arr))
arr.inarray(5)
arr.inarray(29)
arr.insert(4, 50)
arr.inarray(50)
print(arr[3])
print(arr[4])
