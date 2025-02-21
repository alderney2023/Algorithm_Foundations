#############################################################################
#   找到缺失的数字
#   给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
#
#   测试链接 : https://leetcode.cn/problems/missing-number/
#############################################################################

def getMissing(nums):
    n = len(nums)
    eorAll = 0 
    eorHas = 0
    for i in range(n):
        eorAll ^= i
        eorHas ^= nums[i]
    eorAll ^= n
    return eorAll ^ eorHas

def main():
    nums = [0,1,2,3,4,6,7,8,9]
    print(getMissing(nums))  

if __name__ == "__main__":
    main()  