#############################################################################
# 数组中只有1种数出现次数少于m次，其他数都出现了m次
# 返回出现次数小于m次的那种数
#
# 测试链接 : https://leetcode.cn/problems/single-number-ii/
#############################################################################


def singleNumber(nums, m):
    cnts = [0] * 32
    for x in nums:
        for i in range(32):
            cnts[i] += (x >> i) & 1
    res = 0
    for i in range(32):
        if cnts[i] % m != 0:
            res += 2**i
    return res 



def main():
    nums = [2,2,3,5,5,6,6,7,7,8,8]
    print(singleNumber(nums, 2))  

if __name__ == "__main__":
    main()  