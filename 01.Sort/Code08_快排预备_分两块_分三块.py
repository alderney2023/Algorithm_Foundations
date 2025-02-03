
# 1. 给定一个数组arr， 和一个num, 
#    把小于等于num的数放在数组左边，大于num的数放在数组的右边
#    时间复杂度O(N),空间复杂度O(1)。 

# 2. 给定一个数组arr， 和一个num, 
#    把小于num的数放在数组左边，等于num的数放在数组中间，大于num的数放在数组的右边
#    时间复杂度O(N),空间复杂度O(1)。 

import random

#---------------------------------------------------------------------------------

def partitionTwoParts(lst, n):
    if not lst or len(lst) < 2:
        return 
    less = -1
    for i in range(len(lst)):
        if lst[i]<=n:
            lst[i], lst[less+1] = lst[less+1], lst[i]
            less+=1


def partitionThreeParts(lst, n):
    if not lst or len(lst) < 2:
        return 
    less = -1
    more = len(lst)
    i=0
    while i < more:
        if lst[i]<n:
            lst[i], lst[less+1] = lst[less+1], lst[i]
            less += 1
            i += 1
        elif lst[i]>n:
            lst[i], lst[more-1] = lst[more-1], lst[i]
            more -= 1
        else:
            i += 1

#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 20
    maxvalue = 10
    lst = generateRandomList(size,maxvalue)
    print(lst)

    n = 5
    lst1 = lst.copy()
    partitionTwoParts(lst1, n)
    print(lst1)

    lst2 = lst.copy()
    partitionThreeParts(lst2, n)
    print(lst2)


if __name__ == "__main__":
    main()