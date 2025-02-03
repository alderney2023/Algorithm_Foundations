################################################################################################
#   快排1.0 (略)    每次用待排序子序列的最后一个数作为n,迭代切2部分                   O(N**2)
#   快排2.0 (略)    每次用待排序子序列的最后一个数作为n,迭代切3部分                   O(N**2)
#   随机快排        每次用待排序子序列的一个随机数与子序列的最后一个数做交换并作为n     O(NlogN)
################################################################################################


import random

def quickSort(lst):
    if not lst or len(lst) < 2:
        return 
    process_sort(lst, 0, len(lst)-1)

def process_sort(lst, l, r):
    if l >= r:   # >= important
        return 
    #随机快排需要每次迭代，在处理序列中（l和r）之间， 产生一个随机位置和当前序列最后一位交换。
    random_num = l + int(random.random() * (r - l + 1))   
    print(random_num) 
    lst[random_num], lst[r] = lst[r], lst[random_num]

    p1, p2 = partition(lst, l, r)
    process_sort(lst, l, p1-1)
    process_sort(lst, p2+1, r)

def partition(lst, l, r):
    n = lst[r]
    less = l-1
    more = r+1
    while l < more:
        if lst[l] < n:
            lst[l], lst[less+1] = lst[less+1], lst[l]
            less+=1
            l+=1
        elif lst[l] > n:
            lst[l], lst[more-1] = lst[more-1], lst[l]
            more-=1
        else:
            l+=1
    return less+1, more-1
    

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

    quickSort(lst)
    print(lst)

 
if __name__ == "__main__":
    main()