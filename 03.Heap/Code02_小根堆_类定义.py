

class minHeap:


    def __init__(self, heap=[]):
        self._heap = heap
        self._heapsize = len(heap)
        if self._heap:
            for i in range(self._heapsize):
                self._heapInsert(i)
    
    def _heapify(self, index):
        left = 2 * index + 1
        while left < self._heapsize:
            right = left + 1
            if right < self._heapsize and self._heap[right] < self._heap[left]:
                smallest = right
            else:
                smallest = left
            if self._heap[index] <= self._heap[smallest]:
                break
            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            index = smallest
            left = 2 * index + 1

    def _heapInsert(self, index):
        parent = int((index - 1) / 2)
        while self._heap[index] < self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = int((index - 1) / 2)
 
    def heappush(self, value):
        if len(self._heap) > self._heapsize:
            self._heap[self._heapsize] = value
        else:
            self._heap.append(value)
        self._heapInsert(self._heapsize)
        self._heapsize += 1
        
    def heappop(self):
        res = self._heap[0]
        self._heap[0] = self._heap[self._heapsize - 1]
        self._heapsize -= 1
        self._heapify(0)
        return res

    def isEmpty(self):
        return self._heapsize == 0
    
    def heapPrint(self):
        print(self._heap[:self._heapsize])

    def heapsize(self):
        return self._heapsize
    




#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():

    # mh = minHeap()
    # mh.heappush(4)
    # mh.heappush(6)
    # mh.heappush(0)
    # mh.heappush(1)
    # mh.heappush(2)
    # mh.heappush(3)
    # mh.heappush(5)
    # mh.heapPrint()

    # lst = [2,6,4,1,7,9,5]
    # mh = minHeap(lst)
    # mh.heapPrint()

    # lst = [2,6,4,1,7,9,5]
    # mh = minHeap(lst)
    # mh.heapPrint()
    # mh.heappop()
    # mh.heapPrint()
    # mh.heappush(0)
    # mh.heapPrint()

    lst = []
    mh = minHeap(lst)
    mh.heapPrint()
    print(mh.isEmpty())
    print(mh.heapsize())


if __name__ == "__main__":
    main()
