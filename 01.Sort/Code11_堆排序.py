###########################################################################
# 堆排序    O(N*logN)
###########################################################################


import random

def heapSort(heap):
    heapsize = len(heap)
    if not heap or heapsize < 2:
        return 
    # 列表 -> 大根堆
    #O(N*logN)
    # for i in range(heapsize):
    #     heapInsert(heap, i)
    #O(N)
    for i in range((heapsize-1)//2, -1, -1):
        heapify(heap, i, heapsize)

    # 循环在0~j中heapify, 将堆顶数值(当前对最大值)移入最后，j递减
    # O(N*logN)
    for j in range(heapsize-1, 0, -1):   # O(N)
        heap[0], heap[j] = heap[j], heap[0]   
        heapify(heap, 0, j)  # O(logN)
        
def heapInsert(heap, index):
    parent = int((index-1) / 2)
    while heap[index] > heap[parent]: 
        heap[index], heap[parent] = heap[parent], heap[index] 
        index = parent
        parent = int((index-1) / 2)

def heapify(heap, index, heapsize):
    left = index * 2 + 1
    while left < heapsize:
        if left + 1 < heapsize and heap[left+1] > heap[left]:
            largest = left + 1
        else:
            largest = left
        if heap[index] >= heap[largest]:
            break
        heap[index], heap[largest] = heap[largest], heap[index]
        index = largest 
        left = index * 2 + 1



#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():

    #lst = [6, 28, 1, 20, 41, 16, 28, 14, 47, 34]

    for i in range(200):
        maxvalue = 100
        size = generateRandomList(1, maxvalue)[0]
        lst = generateRandomList(size, maxvalue)

        lst1 = lst.copy()
        heapSort(lst1)
        lst2 = lst.copy()
        lst2.sort()

        for j in range(len(lst1)):
            if lst1[j] != lst2[j]:
                print("error:")
                print("lst1:",lst1)
                print("lst2:",lst2)
    print("correct")


if __name__ == "__main__":
    main()
