###########################################################################
# 堆排序    O(N*logN)
# 列用python的heapq实现的小根堆进行堆排序
###########################################################################

import heapq, random

def heapSort(lst):
    minHeap = []
    for x in lst:
        heapq.heappush(minHeap,x)
    sorted_lst = []
    while minHeap:
        sorted_lst.append(heapq.heappop(minHeap))
    return sorted_lst


#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    lst = generateRandomList(10,20)
    sorted_lst = heapSort(lst)
    print(sorted_lst)

if __name__ == "__main__":
    main()
