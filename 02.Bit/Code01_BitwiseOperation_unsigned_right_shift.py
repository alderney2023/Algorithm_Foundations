#############################################################################
# python 没有无符号右移符
#############################################################################

def unsigned_right_shift(value, shift):
    """实现 Java 的无符号右移（>>>）"""
    # 将 a 转换为无符号整数并右移 b 位
    # print(value)
    # print(to_binary(value, bits=64))
    value = value % (1 << 32) 
    # print(value)
    # print(to_binary(value, bits=64))    
    return value >> shift
    #return (value % (1 << 32)) >> shift

def unsigned_right_shift2(value, shift):
    """实现 Java 的无符号右移（>>>）"""
    if value < 0:
        # 将负数转换为补码形式
        # print(value)
        # print(to_binary(value, bits=64))
        value = (1 << 32) + value
        # print(value)
        # print(to_binary(value, bits=64))
    # 限制为 32 位
    value = value & 0xFFFFFFFF
    # 右移
    return value >> shift


#---------------------------------------------------------------------------------

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')

def main():

    value = -1024
    shift = 30

    x = unsigned_right_shift(value, shift)
    print(x)

    y = unsigned_right_shift2(value, shift)
    print(y)



if __name__ == "__main__":
    main()  