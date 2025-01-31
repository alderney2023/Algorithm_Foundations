###########################################################################
# 定义一个大根堆类结构
# 初始化: 可以一个一个push, 也可以赋给一个list
# private functions:  heapify, heapInsert
# public functions: isEmpty, push, pop, printMaxHeap, heapSize
###########################################################################

import random

class MaxHeap():

    def __init__(self, heap=[], heapsize=0):
        self._heap = heap
        self._heapsize = len(heap)
        if self._heap:
            for i in range(self._heapsize):
                self._heapInsert(i)

    def _heapify(self, index):
        left = 2 * index + 1
        while left <= self._heapsize:
            if left + 1 <= self._heapsize and self._heap[left+1] > self._heap[left]:
                largest = left+1
            else:
                largest = left
            if self._heap[index] >= self._heap[largest]:
                break
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            index = largest
            left = 2 * index + 1

    def _heapInsert(self, index):
        parent = int(( index - 1) / 2 )
        while self._heap[index] > self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = int(( index - 1) / 2 )

    def isEmpty(self):
        return self._heapsize == 0

    def push(self, value):
        self._heapsize += 1
        if self._heapsize <= len(self._heap):
            self._heap[self._heapsize-1]=value
        else:
            self._heap.append(value)
        self._heapInsert(self._heapsize-1)

    def pop(self):
        x = self._heap[0]
        self._heap[0] = self._heap[self._heapsize-1]
        self._heapsize-=1
        self._heapify(0)
        return x

    def printMaxHeap(self):
        print(self._heap[:self._heapsize])

    def heapSize(self):
        print(self._heapsize)

#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    # mh = MaxHeap()
    # mh.push(0)
    # mh.push(1)
    # mh.push(2)
    # mh.push(3)
    # mh.push(4)
    # mh.push(5)
    # mh.push(6)
    # mh.printMaxHeap()
    # print("heapsize:",mh.heapsize)

    # x = mh.pop()
    # print(x)
    # mh.printMaxHeap()
    # print("heapsize:",mh.heapsize)


    # lst = generateRandomList(8,10)
    # mh2 = MaxHeap(lst)
    # mh2.printMaxHeap()
    # mh2.heapSize() 

    # x = mh2.pop()
    # mh2.printMaxHeap()
    # mh2.heapSize()

    # mh2.push(11)
    # mh2.printMaxHeap()
    # mh2.heapSize()

    # mh2.push(12)
    # mh2.printMaxHeap()
    # mh2.heapSize()

    # x = mh2.pop()
    # mh2.printMaxHeap()
    # mh2.heapSize()

    # print(mh2.isEmpty())

    mh3 = MaxHeap([])
    print(mh3.isEmpty())  
    mh3.printMaxHeap()
    mh3.heapSize()


if __name__ == "__main__":
    main()





#---------------------------------------------------------------------------------

