#########################################################################################
# 已知一个几乎有序的数组， 
# 几乎有序是指，如果把数组排好顺序的话，每个元素移动的距离可以不超过k,并且k相对于数组来说比较小
# 选择一个合适的排序算法针对这个数据进项排序
#########################################################################################


import random, heapq

def sortListDistanceLessK(lst,k):
    n = len(lst)
    if not lst or n<2:
        return 
    #前K个进堆
    minheap = []
    for i in range(min(k, n)):
        heapq.heappush(minheap, lst[i])
    #每进一个数入堆，出堆顶最大值，往后移一位
    j=0
    for i in range(k, n):
        heapq.heappush(minheap, lst[i])
        lst[j] = heapq.heappop(minheap)
        j+=1
    #将剩余堆内数字一个个写回列表
    while minheap:
        lst[j] = heapq.heappop(minheap)
        j+=1


#---------------------------------------------------------------------------------

def randomArrayNoMoveMoreK(size, maxvalue, k):
    lst = []
    for i in range(size):
        x = int(random.random()* (maxvalue + 1))
        lst.append(x)
    lst.sort()

    isSwap = [0] * size
    for i in range(size):
        j = min(i + int(random.random() * (k + 1)), size - 1)
        if (not isSwap[i] and not isSwap[j]):
            isSwap[i], isSwap[j] = 1, 1		
            lst[i], lst[j] = lst[j], lst[i]
    return lst


def main():
    size = 10
    maxvalue = 20
    k = 3
    lst = randomArrayNoMoveMoreK(size, maxvalue, k) 
    print(lst)
    sortListDistanceLessK(lst, k)
    print(lst)


if __name__ == "__main__":
    main()