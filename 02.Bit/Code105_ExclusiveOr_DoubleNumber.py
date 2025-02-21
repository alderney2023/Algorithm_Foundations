#############################################################################
# 数组中有2种数出现了奇数次，其他的数都出现了偶数次
# 返回这2种出现了奇数次的数
#
# 测试链接 : https://leetcode.cn/problems/single-number-iii/
#############################################################################

def singleNumber(nums):
    eor1 = 0 
    for x in nums:
        eor1 ^= x
    rightOne = eor1 & (~eor1 + 1)
    eor2 = 0
    for x in nums:
        if x & rightOne == 0:
            eor2 ^= x
    return eor2, eor1^eor2

def main():
    nums = [2,2,3,5,5,6,6,6,7,7]
    print(singleNumber(nums))  

if __name__ == "__main__":
    main()  