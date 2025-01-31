###########################################################################
# 计数排序    O(N)
# 桶排序的一种，不基于比较
###########################################################################



import random

def countSort(lst):
    maxvalue = lst[0]
    for x in lst:
        if x > maxvalue:
            maxvalue = x
    bucket = [0] * (maxvalue+1)
    for x in lst:
        bucket[x] +=1
    j = 0
    for i in range(maxvalue+1):
        while bucket[i]:
            lst[j] = i
            j+=1
            bucket[i]-=1

#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 50
    maxvalue = 20
    lst = generateRandomList(size,maxvalue)
    print(lst)
    countSort(lst)
    print(lst)

if __name__ == "__main__":
    main()
