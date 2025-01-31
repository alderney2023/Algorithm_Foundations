#########################################################
# 列表中逆序对的数量    （用merge sort排逆序）
#########################################################

import random

#---------------------------------------------------------------------------------
# 归并排序 递归方式
def reversePairsCount(lst):
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
    cnt = 0
    p1, p2 = l, mid+1
    while p1<=mid and p2<=r:
        #print("p1:", p1, "p2:", p2)
        if lst[p1] > lst[p2]:     #逻辑是处理大于， 小于等于放入else
            help.append(lst[p1])
            cnt += r-p2+1
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
    return cnt

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

    lst1 = lst.copy()
    cnt = reversePairsCount(lst1)  #递归方法
    print(lst1)
    print(cnt)

    reverse_pairs_cnt = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                reverse_pairs_cnt +=1
    print(reverse_pairs_cnt)

if __name__ == "__main__":
    main()