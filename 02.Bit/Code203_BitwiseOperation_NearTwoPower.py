#############################################################################
# 已知n是非负数
# 返回大于等于n的最小的2某次方
# 如果int范围内不存在这样的数，返回整数最小值
#############################################################################

def nearTwoPower(n):
    n -= 1
    i = 1
    while i <=32:
        n |= n >> i
        i *= 2
    return n+1



def main():   
    x = nearTwoPower(31)
    print(x, bin(x))
    x = nearTwoPower(33)
    print(x, bin(x))
    x = nearTwoPower(2**16 - 2)
    print(x, bin(x))

if __name__ == "__main__":
    main()   