#########################################################
#   选择排序    O(N**2)
#   冒泡排序    O(N**2)
#   插入排序    O(N**2)
#########################################################
#   

import random


def selectionSort(l):
    if not l or len(l) < 2:
        return 
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

def bubbleSort(l):
    if not l or len(l) < 2:
        return 
    for i in range(len(l)-1, -1, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

def insertionSort(l):
    if not l or len(l) < 2:
        return 
    for i in range(1,len(l)):
        j = i 
        while l[j] < l[j-1] and j>0:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1




def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    lst1 = generateRandomList(30,100)
    print(lst1)

    lst2 = lst1.copy()
    lst3 = lst1.copy()
    lst4 = lst1.copy()

    lst1.sort()
    print(lst1)

    selectionSort(lst2)
    print(lst2)

    bubbleSort(lst3)
    print(lst3)

    insertionSort(lst4)
    print(lst4)


if __name__ == "__main__":
    main()