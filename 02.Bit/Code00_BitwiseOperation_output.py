#############################################################################
# bin, format
#############################################################################

# 另，python需要自己去手动处理溢出和符号扩展等问题。
#     比如：   (n << shirt_amount) & 0xFFFFFFFF
          

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')


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


 





if __name__ == "__main__":
    main()   