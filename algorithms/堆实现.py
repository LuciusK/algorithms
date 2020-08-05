class Array(object):
    """
    Achieve an Array by Python list
    """
    def __init__(self, size = 32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        """
        Get items
        :param index: get a value by index
        :return: value
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        set item
        :param index: giving a index you want to teset
        :param value: the value you want to set
        :return:
        """
        self._items[index] = value

    def __len__(self):
        """
        :return: the length of array
        """
        return self._size

    def clear(self, value=None):
        """
        clear the Array
        :param value: set all value to None
        :return: None
        """
        for i in range(self._size):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MinHeap(object):
    """
    Achieve a minimum heap by Array
    """

    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        """
        Add an element to heap while keeping the attribute of heap unchanged.
        :param value: the value added to the heap
        :return: None
        """
        if self._count >= self.maxsize:
            raise Exception("The heap is full!")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, index):
        """
        To keep the the attribute of heap unchanged while adding a new value.
        :param index: the index of value you want to swap
        :return: None
        """
        if index > 0:
            parent = int((index - 1) / 2)
            if self._elements[parent] > self._elements[index]:
                self._elements[parent], self._elements[index] = self._elements[index], self._elements[parent]
                self._siftup(parent)

    def extract(self):
        """
        pop and return the value of root
        :return: the value of root
        """
        if self._count <= 0:
            raise Exception('The heap is empty!')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, index):
        """
        to keep the attribute of heap unchanged while pop out the root node.
        :param index: the index of value you want to swap
        :return: None
        """
        if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < self._count and right < self._count \
                and self._elements[left] <= self._elements[right] \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)
            elif left < self._count and right < self._count \
                and self._elements[left] >= self._elements[right] \
                and self._elements[right] <= self._elements[index]:
                self._elements[right], self._elements[index] = self._elements[index], self._elements[right]
                self._siftdown(left)

            if left < self._count and right > self._count \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)

if __name__ == '__main__':
    import random
    n = 5
    h = MinHeap(n)
    for i in range(n):
        h.add(i)
    for i in range(n):
        assert i == h.extract()
