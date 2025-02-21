#############################################################################
# 取最右边的1
#############################################################################

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')


def main():

    a = -10
    print(to_binary(a, bits=8))

    #方法一
    b = a &(-a) 
    print(to_binary(b, bits=8))

    #方法二
    c = a & (~a + 1) 
    print(to_binary(c, bits=8))
    print("-----------------")

if __name__ == "__main__":
    main()   