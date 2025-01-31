
import random

def radixSort(lst):
    n = len(lst)
    if not list or n < 2:
        return 
    #获得最大值，及它有几位
    maxbits = maxBits(lst) 
    #从个位往高位循环
    radix = 10
    for d in range(1,maxbits+1):
        counts = [0] * radix
        #每个数出现的次数, 如 count[3] = 2， 表示有2个数此位是3
        for x in lst:
            t = get_digit(x, d)
            counts[t] += 1
        #累加和, 如 count[3] = 5， 表示在此位上小于等于3的有5个数
        for i in range(1, radix):
            counts[i] += counts[i-1]
        #从右往左遍历，按此位的排好序， 写入help
        help = [0] * n 
        for i in range(n-1, -1, -1):
            t = get_digit(lst[i], d)
            help [counts[t] - 1 ] =  lst[i]
            counts[t] -= 1
        #写回lst
        for j in range(n):
            lst[j] = help[j]


def maxBits(lst):
    maxvalue = lst[0]
    for x in lst:
        if x > maxvalue:
            maxvalue = x
    n=0
    while maxvalue:
        maxvalue = maxvalue // 10
        n+=1
    return n


def get_digit(x, d):
     x = x // int (10** (d-1))
     x = x%10
     return x


#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    size = 10
    maxvalue = 2000
    lst = generateRandomList(size,maxvalue)
    print(lst)
    radixSort(lst)
    print(lst)


if __name__ == "__main__":
    main()