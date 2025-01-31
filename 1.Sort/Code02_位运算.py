#########################################################
# 在一个数组中找到唯一一个只出现奇数次的数
# 在一个数组中找到两个只出现奇数次的不同的数
#########################################################


#在一个数组中找到唯一一个只出现奇数次的数
def oneOddTimesNum(lst):
    eor = 0 
    for x in lst:
        eor ^= x
    return eor

#在一个数组中找到两个只出现奇数次的不同的数
def twoOddTimesNums(lst):
    eor = 0 
    for x in lst:
        eor ^= x
    rightone = eor & (~eor+1)
    a = 0
    for x in lst:
        if rightone & x == 0:
            a ^= x
    b = eor ^ a
    return a,b

    
def main():
    #在一个数组中找到唯一一个只出现奇数次的数
    l1 = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5]
    print(oneOddTimesNum(l1))

    #在一个数组中找到两个只出现奇数次的不同的数
    l2 = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5]
    print(twoOddTimesNums(l2))
    
    
if __name__ == "__main__":
    main()