#########################################################
# 在有序序列中，查找某个数是否存在
# 在有序序列中，找到>=n的最左边值的下标
# 在有序序列中，找到<=n的最右边值的下标
# 在一个相邻不等的无序序列中，找到一个局部最小值的下标
#########################################################


import random

#---------------------------------------------------------------------------------
# 在有序序列中查找某个数是否存在
def bsexist(lst, n):
    if not lst or len(lst)==0:
        return -1
    l, r = 0, len(lst)-1
    while l < r:
        mid = l + ((r-l)>>1)
        if n == lst[mid]:
            return mid
        elif n < lst[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if lst[l] == n:
        return l
    else:
        return -1

# better
def bsexist2(lst, n):
    if not lst or len(lst)==0:
        return -1
    l, r = 0, len(lst)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        #print("l:",l, "r:",r, "mid:", mid)
        if n == lst[mid]:
            return mid
        elif n < lst[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


#---------------------------------------------------------------------------------
# 在有序序列中，找到>=n的最左边值的下标
def bsleft(lst, n):
    if not lst or len(lst)==0:
        return -1
    l, r = 0, len(lst)-1
    index = -1
    while l <= r:
        mid = l + ((r-l)>>1)
        if lst[mid] >= n:
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    return index
        

#---------------------------------------------------------------------------------
# 在有序序列中，找到<=n的最右边值的下标
def bsright(lst, n):
    if not list or len(lst) == 0:
        return -1
    l, r = 0, len(lst)-1
    index = -1
    while l<=r:
        mid = l + ((r-l)>>1)
        #print("l:",l, "r:",r, "mid:", mid)
        if lst[mid]<=n:
            index = mid
            l = mid + 1
        else:
            r = mid - 1
    return index


#---------------------------------------------------------------------------------
# 在一个相邻不等的无序序列中，找到一个局部最小值的下标
def local_min(lst):
    if not lst or len(lst) == 0:
        return -1
    if len(lst) == 1 or lst[0] < lst[1]:
        return 0
    if lst[len(lst)-1] < lst[len(lst)-2]:
        return len(lst)-1

    l, r = 0, len(lst)-1
    while l<=r:
        mid = l + ((r-l)>>1)
        if lst[mid] < lst[mid-1] and lst[mid] < lst[mid+1]:
            return mid
        elif lst[mid] > lst[mid-1]:
            r = mid
        else:
            l = mid
    

#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def generateRandomListNoNearEqual(size,maxvalue):
    lst = []
    lst.append(int(random.random()*maxvalue) + 1)
    i = 1
    while i < size:
        x = int(random.random()*maxvalue) + 1
        if x != lst[i-1] :
            lst.append(x)
            i+=1
    return lst


def main():

    lst = generateRandomList(20,10)
    lst.sort()
    n = generateRandomList(1,10)[0]
    print(lst, n)

    # 在有序序列中，查找某个数是否存在
    print(bsexist(lst,n))
    print(bsexist2(lst,n))

    # 在有序序列中，找到>=n的最左边值的下标
    print(">=n most left:", bsleft(lst,n))
    i = 0
    while i<len(lst) and lst[i]<n:
        i+=1
    print("check:",i)
 
    # 在有序序列中，找到<=n的最右边值的下标
    print("<=n most right:", bsright(lst,n))
    i = len(lst) -1
    while i>=0 and lst[i]>n:
        i-=1
    print("check:",i)

    # 在一个相邻不等的无序序列中，找到一个局部最小值的下标
    lst2 = generateRandomListNoNearEqual(30,50)
    print(lst2)
    i = local_min(lst2)
    print("local min:", i)
    check = ( len(lst2)<=1 ) or \
            ( i==0 and lst2[0]<lst2[1]) or \
            ( i==len(lst2)-1 and lst2[len(lst2)-1] < lst2[len(lst2)-2] ) or \
            ( lst2[i]<lst2[i-1] and lst2[i]<lst2[i+1] )
    print("check:", check)


if __name__ == "__main__":
    main()