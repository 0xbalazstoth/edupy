# super() függvény: Ősosztály teljes tulajdonságait és viselkedését örökli a gyermekosztály


# Fix méretű tömb
class FixedSizeList(list):
    def __init__(self, size, *args):
        self.size = size
        super().__init__(*args)
        if len(self) > self.size:
            raise ValueError(f"List exceeds fixed size of {self.size}")

    def append(self, item):
        if len(self) >= self.size:
            raise IndexError("Appending to a fixed-size list")
        super().append(item)

    def insert(self, index, item):
        if len(self) >= self.size:
            raise IndexError("Inserting to a fixed-size list")
        super().insert(index, item)

    def extend(self, iterable):
        if len(self) + len(iterable) > self.size:
            raise IndexError("Extending a fixed-size list")
        super().extend(iterable)

    def __setitem__(self, index, value):
        if index >= self.size:
            raise IndexError("Assignment index out of range")
        super().__setitem__(index, value)

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        return super().__getitem__(index)


# Usage
fixed_list = FixedSizeList(5, [1, 2, 3])
print(fixed_list)  # Output: [1, 2, 3]

fixed_list.append(4)
fixed_list.append(5)
print(fixed_list)  # Output: [1, 2, 3, 4, 5]

# This will raise an IndexError
try:
    fixed_list.append(6)
except IndexError as e:
    print(e)  # Output: Appending to a fixed-size list

# This will also raise an IndexError
try:
    fixed_list.extend([6, 7])
except IndexError as e:
    print(e)  # Output: Extending a fixed-size list
