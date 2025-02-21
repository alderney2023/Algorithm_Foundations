

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')

def unsigned_right_shift(a, b):
    # 将 a 转换为无符号整数并右移 b 位
    return (a % (1 << 32)) >> b

def main():

    #输出非负数的二进制数
    a = 10
    print(bin(a))
    print(format(a,'08b'))
    print(to_binary(a, bits=8))
    print("-----------------")
          
    #输出负数的二进制数
    b = -10
    print(bin(b))
    print(format(b,'08b'))
    print(format(b & 0b11111111,'08b'))
    print(format(b & 0xff,'08b'))
    print(to_binary(b, bits=8))
    print("-----------------")


    #取最右边的1
    a = -10
    b = a &(-a) #方法一
    print(a, to_binary(b, bits=8))
    c = a & (~a + 1) #方法二
    print(a, to_binary(c, bits=8))
    print("-----------------")

    a = -1024
    move = 30
    print(a,to_binary(a, bits=32))
    x = a % (1 << 32)
    print(x,to_binary(x, bits=32))
    y = x >> move 
    print(y,to_binary(y, bits=32))


    # print(a,to_binary(a, bits=32))
    # b = unsigned_right_shift(a, move)
    # print(b,to_binary(b, bits=32))



if __name__ == "__main__":
    main()   