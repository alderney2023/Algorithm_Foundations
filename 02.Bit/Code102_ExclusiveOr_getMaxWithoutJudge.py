#############################################################################
#   不用任何判断语句和比较操作，返回两个数的最大值
#############################################################################

#入参只能是0或1，将0变1，1变0
def flip(n):
    return n^1

#非负返回1， 负数返回0
def sign(n):
    x = (n % 0x100000000) >> 31 
    return flip(x)

#有溢出风险
def getMax1(a, b):
    c = a - b
    returnA = sign(c)        # if a大 -> c非负 -> 1; if b大 -> c为负 -> 0
    returnB = flip(returnA)  # if a大 -> 0 ;         if b大 -> 1
    return a * returnA  + b * returnB 

#没有任何问题
def getMax2(a, b):
    c = a - b
    sa = sign(a)    # if a非负 -> 1;    if a为负 -> 0
    sb = sign(b)    # if b非负 -> 1;    if b为负 -> 0
    sc = sign(c)    # if a大 -> c非负 -> 1; if b大 -> c为负 -> 0
    diffAB = sa ^ sb        # a,b符号不同 -> 1;    a,b符号相同 -> 0
    sameAB = flip(diffAB)   # a,b符号相同 -> 1;    a,b符号不同 -> 0
    
    # if a,b符号不同，a为负， 1 * 0 + 0 * sc = 0;
    #                a非负， 1 * 1 + 0 * sc = 1
    # if a,b符号相同，a为负， 0 * 0 + 1 * sc = sc (a大，1； a小， 0)
    #                a非负， 0 * 1 + 1 * sc = sc (a大，1； a小， 0)
    returnA = diffAB * sa + sameAB * sc  

    # if a,b符号不同，b为负， 1 * 0 + 0 * sc = 0;
    #                b非负， 1 * 1 + 0 * sc = 1
    # if a,b符号相同，b为负， 0 * 0 + 1 * sc = sc (b大，1； b小， 0)
    #                b非负， 0 * 1 + 1 * sc = sc (b大，1； b小， 0)     
    returnB = diffAB * sb + sameAB * sc

    # if a,b符号不同，返回非负的
    # if a,b符号相同，返回大的
    return a * returnA  + b * returnB 



def main():
    a = 2**31 - 1
    b = -2**31
    print(getMax1(a, b))  #溢出， 错误
    print(getMax2(a, b))  #正确

    a = 100
    b = -100
    print(getMax1(a, b))  #正确
    print(getMax2(a, b))  #正确

if __name__ == "__main__":
    main()  