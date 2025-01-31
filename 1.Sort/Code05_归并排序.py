#########################################################
# 归并排序 递归方式   （ 二分切片 ）
# 归并排序 非递归方式 （ 以1，2，4，8...切片 ）

# O(NlogN)
#########################################################

import random

#---------------------------------------------------------------------------------
# 归并排序 递归方式
def mergeSort1(lst):
    n = len(lst)
    if not lst or n < 2:
        return 
    process(lst, 0, n-1)

def process(lst, l, r):
    if l == r:
        return 
    mid = l + ((r-l)>>1)
    process(lst, l, mid)
    process(lst, mid+1, r)
    merge(lst, l, mid, r)
    #print(lst)

def merge(lst, l, mid, r):
    help = []
    p1, p2 = l, mid+1
    while p1<=mid and p2<=r:
        #print("p1:", p1, "p2:", p2)
        if lst[p1] <= lst[p2]:
            help.append(lst[p1])
            p1+=1
        else:
            help.append(lst[p2])
            p2+=1
    while p1<=mid:
        help.append(lst[p1])
        p1+=1
    while p2<=r:
        help.append(lst[p2])
        p2+=1
    for i in range(r-l+1):
        lst[l+i] = help[i]


#---------------------------------------------------------------------------------
# 归并排序 非递归方式
def mergeSort2(lst):
    n = len(lst)
    if not lst or n<2:
        return
    merge_size = 1
    while merge_size < n:
        l = 0
        mid = l + merge_size - 1 
        while mid < n:  
            r = min(mid+merge_size,n-1) 
            #print(l,mid,r)
            merge(lst,l,mid,r)
            #print(lst)
            l = r+1
            mid = l + merge_size - 1 
        merge_size <<= 1


#---------------------------------------------------------------------------------
def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    #l=[1,5,3,7,2,8,4,9,4,8]
    size = 20
    maxvalue = 20
    lst = generateRandomList(size,maxvalue)
    print(lst)

    lst1 = lst.copy()
    mergeSort1(lst1)  #递归方法
    print(lst1)

    lst2 = lst.copy()
    mergeSort2(lst2)  #非递归方法
    print(lst2)

if __name__ == "__main__":
    main()