#############################################################################
# 数组中1种数出现了奇数次，其他的数都出现了偶数次
# 返回出现了奇数次的数
#
# 测试链接 : https://leetcode.cn/problems/single-number/
#############################################################################

def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x
    return res

def main():
    nums = [2,2,3,4,3,5,5,]
    print(singleNumber(nums))  

if __name__ == "__main__":
    main()  