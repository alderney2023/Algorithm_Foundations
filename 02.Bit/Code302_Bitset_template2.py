#############################################################################
# 位图的实现
# Bitset是一种能以紧凑形式存储位的数据结构
# Bitset(int n) : 初始化n个位，所有位都是0
# void fix(int i) : 将下标i的位上的值更新为1
# void unfix(int i) : 将下标i的位上的值更新为0
# void flip() : 翻转所有位的值  （此方法没有实际反转所有位的值，而是更改0，1的意义，只有在toString时反转取值）
# boolean all() : 是否所有位都是1
# boolean one() : 是否至少有一位是1
# int count() : 返回所有位中1的数量
# String toString() : 返回所有位的状态
#
#测试链接 : https://leetcode-cn.com/problems/design-bitset/
#############################################################################

class Bitset:

    def __init__(self, size: int):
        # 使用位图来存储数据，每32位为一组
        self.bits = [0] * ((size + 31) // 32)
        self.size = size
        self.ones = 0  # 当前1的数量， 反转后代表0的数量
        self.zeros = size  # 当前0的数量，反转后代表1的数量
        self.reverse = False  # 是否为反转状态

    def fix(self, idx: int) -> None:
        index = idx // 32
        bit = idx % 32
        if self.reverse: # 
            # 在反转状态下，0表示已设置（有值），1表示未设置（无值）
            if (self.bits[index] & (1 << bit)) != 0:  # 当前位为1（即未设置）
                self.bits[index] ^= (1 << bit)  # 将该位置为0（已设置）
                self.ones += 1  # 此时代表0的个数，因为0代表有值
                self.zeros -= 1 # 此时代表1的个数，因为1代表无值
        else:
            # 在正常状态下，0表示未设置（无值），1表示已设置（有值）
            if (self.bits[index] & (1 << bit)) == 0:  # 当前位为0（即未设置）
                self.bits[index] |= (1 << bit)  # 将该位置为1（已设置）
                self.zeros -= 1
                self.ones += 1

    def unfix(self, idx: int) -> None:
        index = idx // 32
        bit = idx % 32
        if self.reverse:
            # 在反转状态下，0表示已设置（有值），1表示未设置（无值）
            if (self.bits[index] & (1 << bit)) == 0:  # 当前位为0（即已设置）
                self.bits[index] |= (1 << bit)  # 将该位置为1（未设置）
                self.ones -= 1  # 此时代表0的个数，因为0代表有值
                self.zeros += 1  # 此时代表1的个数，因为1代表无值
        else:
            # 在正常状态下，1表示已设置（有值），0表示未设置（无值）
            if (self.bits[index] & (1 << bit)) != 0:  # 当前位为1（即已设置）
                self.bits[index] ^= (1 << bit)  # 将该位置为0（未设置）
                self.zeros += 1
                self.ones -= 1

    # 反转： 原来有n个有值，反转后变成size-n个有值
    def flip(self) -> None:
        # 切换反转状态
        self.reverse = not self.reverse
        # 交换ones和zeros的计数
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        # 判断是否所有位都是已设置状态
        return self.ones == self.size

    def one(self) -> bool:
        # 判断是否至少有一个位是已设置状态
        return self.ones > 0

    def count(self) -> int:
        # 返回已设置（有值）位的数量
        return self.ones

    def toString(self) -> str:
        # 返回当前bitset的字符串表示
        res = []
        for i in range(self.size):
            index = i // 32
            bit = i % 32
            # 获取当前位的状态
            s = (self.bits[index] >> bit) & 1
            # 根据反转状态调整输出值
            if self.reverse:
                s ^= 1  # 在反转模式下，反转0和1的表示
            res.append(str(s))
        return ''.join(res)
#---------------------------------------------------------------------------------

def to_binary(num, bits=8):
    """将整数转换为指定位数的二进制字符串"""
    if num < 0:
        # 处理负数（补码表示）
        return format((1 << bits) + num, f'0{bits}b')
    else:
        return format(num, f'0{bits}b')

def main():   
    bs = Bitset(5)
    bs.fix(3)
    # print(bs.zeros, bs.ones)
    # bs.flip()
    # print(bs.zeros, bs.ones)
    # for x in bs.bits:
    #     print(to_binary(x, 32))  
    # bs.unfix(1)
    # print(bs.zeros, bs.ones)
    # for x in bs.bits:
    #     print(to_binary(x, 32))  

    print(bs.toString())
  



if __name__ == "__main__":
    main()   