###########################################################################
# 一个数据流中，随时可以取得中位数
#   利用一个大根堆，一个小根堆
###########################################################################

import heapq, random

def getMediam(lst):
    leftmaxheap = []
    rightminheap = []
    heapq.heappush(leftmaxheap, (-lst[0], lst[0]))
    for i in range(1,len(lst)):
        if lst[i] < leftmaxheap[0][1]:
            heapq.heappush(leftmaxheap, (-lst[i],lst[i]))
        else:
            heapq.heappush(rightminheap, lst[i])
        if len(leftmaxheap) - len(rightminheap) >= 2:
            _,x = heapq.heappop(leftmaxheap)
            heapq.heappush(rightminheap, x)
        elif len(rightminheap) - len(leftmaxheap) >= 2:
            x = heapq.heappop(rightminheap)
            heapq.heappush(leftmaxheap, (-x, x))

    print(leftmaxheap)
    print(rightminheap)
    if len(leftmaxheap) == len(rightminheap):
        return (leftmaxheap[0][1] + rightminheap[0]) / 2
    elif len(leftmaxheap) > len(rightminheap):
        return leftmaxheap[0][1]
    else:
        return rightminheap[0]

#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 20
    maxvalue = 20
    lst = generateRandomList(size,maxvalue)
    print(lst)
    print(getMediam(lst))
    print("check:")
    print(sorted(lst))


if __name__ == "__main__":
    main()