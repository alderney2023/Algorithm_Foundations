#########################################################
# 用递归方法求列表中的最大值
#########################################################

import random

#---------------------------------------------------------------------------------
def getMax(lst):
    n = len(lst)
    if not lst or n == 0:
        return 0
    return process(lst, 0, n-1)

def process(lst, l, r):
    if l==r:
        return lst[l]
    mid = l + ((r-l)>>1)
    left_max = process(lst, l, mid)
    right_max = process(lst, mid+1, r)
    return max(left_max, right_max)


#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 20
    maxvalue = 30
    lst = generateRandomList(size,maxvalue)
    print(getMax(lst))
    print("check:", max(lst))

if __name__ == "__main__":
    main()