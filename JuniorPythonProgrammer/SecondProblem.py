# ---------------------------------------
# SECOND PROBLEM
# ---------------------------------------

# For n calls works O(2n) which also can be equal to O(n), but this constant.)))
# The big Advantage is that we can look for the element using index in O(1).
class ArrayFIFO:
    # capacity should be bigger than 0
    def __init__(self, capacity=1):
        capacity = max(capacity, 1)
        self.__capacity = capacity
        self.__array = [0] * capacity
        self.__first = 0
        self.__size = 0

    def getAndDel(self):
        res = self.get()
        self.__first = (self.__first + 1) % self.__capacity
        self.__size -= 1
        return res

    def get(self, index=0):
        if index < self.__size:
            return self.__array[(self.__first + index) % self.__capacity]
        elif index == 0:
            raise ValueError("There is no elements in FIFO class")
        else:
            raise ValueError("Index out of bounds")

    def put(self, el):
        if self.__size == self.__capacity:
            self.__extend(2 * self.__capacity + 1)
        self.__array[self.__last()] = el
        self.__size += 1

    def size(self):
        return self.__size

    def __extend(self, capacity):
        newArray = []
        size = self.size()
        for i in range(self.__size):
            newArray.append(self.getAndDel())
        newArray += [0] * (capacity - size)
        self.__size = size
        self.__array = newArray
        self.__first = 0
        self.__capacity = capacity

    def __last(self):
        if self.__size == 0:
            return self.__first
        else:
            return (self.__first + self.__size - 1) % self.__capacity + 1


# For n calls works in O(n). No extra work.
# To look for some element in middle works about O(n).
class LinkedFIFO:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def getAndDel(self):
        res = self.get()
        self.__first = self.__first.next
        self.__size -= 1
        return res

    def get(self):
        if self.size() != 0:
            return self.__first.val
        else:
            raise ValueError("There is no elements in FIFO class")

    def put(self, el):
        if self.size() == 0:
            self.__first = self.Node(el)
            self.__last = self.__first
        else:
            self.__last.next = self.Node(el)
            self.__last = self.__last.next
        self.__size += 1

    def size(self):
        return self.__size

    class Node:
        def __init__(self, el=None, next=None):
            self.val = el
            self.next = next


def testArrayFIFO():
    fifo = ArrayFIFO()
    fifo.put(3)
    fifo.put(4)
    print(fifo.getAndDel())
    print(fifo.getAndDel())
    fifo.put(100)
    print(fifo.getAndDel())
    fifo.put(5)
    print(fifo.getAndDel())
    fifo.put(6)
    print(fifo.getAndDel())
    fifo.put(121)
    print(fifo.getAndDel())


def testLinkedFIFO():
    fifo = LinkedFIFO()
    fifo.put(9)
    fifo.put(46)
    print(fifo.getAndDel())
    print(fifo.getAndDel())
    fifo.put(102)
    print(fifo.getAndDel())
    fifo.put(99)
    print(fifo.getAndDel())
    fifo.put(6)
    print(fifo.getAndDel())
    fifo.put(121)
    print(fifo.getAndDel())


# Hello, here I will code and test problems that
# I got like a test for Junior Python Programmer position.
if __name__ == '__main__':
    testArrayFIFO()

    testLinkedFIFO()
