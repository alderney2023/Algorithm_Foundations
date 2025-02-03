#########################################################
# 求数组小和   （ merge 时 相等取右侧）
# 在一个数组中，一个数左边比它小的总和，叫数的小和。
# 所有数的小和的累加叫做数组小和，求数组小和
#########################################################

import random

#---------------------------------------------------------------------------------
def smallSum(lst):
    n = len(lst)
    if not lst or n < 2:
        return 0
    return process(lst, 0, n-1)

def process(lst, l, r):
    if l == r:
        return 0
    mid = l + ((r-l)>>1)
    return process(lst, l, mid) + process(lst, mid+1, r) + merge(lst, l, mid, r)
    
def merge(lst, l, mid, r):
    help = []
    sum = 0       #
    p1, p2 = l, mid+1
    while p1<=mid and p2<=r:
        #print("p1:", p1, "p2:", p2)
        if lst[p1] < lst[p2]:      #和merge sort不同，改为小于。 即：相同取右侧
            help.append(lst[p1])
            sum += lst[p1] * (r-p2+1)  #
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
    
    return sum


#---------------------------------------------------------------------------------
def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 10
    maxvalue = 20
    lst = generateRandomList(size,maxvalue)
    print(lst)

    lst1 = lst.copy()
    small_sum = smallSum(lst1)  
    print(small_sum)

    small_sum_check = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                small_sum_check += lst[i]
    print("check:", small_sum_check)


if __name__ == "__main__":
    main()