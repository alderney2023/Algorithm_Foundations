#############################################################################
# 不用任何算术运算，只用位运算实现加减乘除
# 代码实现中你找不到任何一个算术运算符
#
# 除法测试链接 : https://leetcode.cn/problems/divide-two-integers/
#############################################################################



#---------------------------------------------------------------------------------


def add(a, b):
    res = a
    while b:
        res = a ^ b
        b = ((a & b) << 1) & 0xFFFFFFFF     #  左移一定要加
        a = res
    return res

def neg(a):
    return add(~a, 1)

def minus(a, b):
    return add(a, neg(b))

def multiply(a, b):
    # a = a if a >= 0 else neg(a)
    # b = b if b >= 0 else neg(b)
    a = abs(a)
    b = abs(b)
    res = 0
    while b:
        if b & 1 == 1:
            res = add(res, a)
        b >>= 1
        a <<= 1
    return res if ( (a < 0) ^ (b < 0)) else neg(res)

def divide(a, b):
    if a == -2147483648 and b == -1:
        return 2147483647
    if a != -2147483648 and b == -2147483648:
        return 0
    

    negative = (a < 0) != (b < 0)  # 判断符号，结果负数时返回True

    x = abs(a)
    y = abs(b)
    res = 0
    for i in range(31, -1, -1):
        if (x >> i) >= y:
            res |= (1 << i)  
            x = minus(x, (y << i))  
    return neg(res) if negative else res



#---------------------------------------------------------------------------------


def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')

def main():   
    a, b = 3, -25
    print(add(a,b))
    print(minus(a,b))
    print(multiply(a,b))

    a, b = 3, -25
    print(divide(b,a))

    # a,b均为32位整数最小值
    a, b =  -2147483648, -2147483648
    print(divide(a,b))

    # b为32位整数最小值
    a, b =  4444, -2147483648
    print(divide(a,b))

    a, b =  -2147483648, 4444
    print(divide(a,b))

if __name__ == "__main__":
    main()   