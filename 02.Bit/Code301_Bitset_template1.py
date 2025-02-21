#############################################################################
# 位图的实现
# Bitset(int size)
# void add(int num)
# void remove(int num)
# void reverse(int num)
# boolean contains(int num)
#############################################################################

class bitset:
    def __init__(self, n):
        self.bits = [0] * ((n+31)//32)
    
    def add(self, num):
        self.bits[num//32] |=  (1 << (num%32))

    def remove(self, num):
        self.bits[num//32] &= 0 << num%32

    def reverse(self, num):
        self.bits[num//32] ^= 1 << num%32

    def contains(self, num):
        return (self.bits[num//32] >> num%32) & 1 == 1
        

#---------------------------------------------------------------------------------

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')

def main():   
    bs = bitset(100)
    bs.add(97)
    print(bs.contains(97))
    print(bs.contains(96))

    for x in bs.bits:
        print(to_binary(x, 32))
    bs.reverse(97)
    for x in bs.bits:
        print(to_binary(x, 32))   

    bs.add(88)
    print(bs.contains(88))
    bs.remove(88)
    print(bs.contains(88))



if __name__ == "__main__":
    main()   