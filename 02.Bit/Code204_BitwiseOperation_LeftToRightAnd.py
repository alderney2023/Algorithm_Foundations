#############################################################################
# 给你两个整数 left 和 right ，表示区间 [left, right]
# 返回此区间内所有数字 & 的结果
# 包含 left 、right 端点
#
# 测试链接 : https://leetcode.cn/problems/bitwise-and-of-numbers-range/

# 方法一：最优，Brian Kernighan 算法
# 方法二：次优，每位一次检查
# 方法三：暴力
#############################################################################


#---------------------------------------------------------------------------------
# 方法一： Brian Kernighan 算法

def rangeBitwiseAnd1(left, right):
    while left < right :
        rightOne = right & -right
        right -= rightOne
    return right


#---------------------------------------------------------------------------------
# 方法二：每位一次检查

def rangeBitwiseAnd2(left, right):
    shift = 0 
    while (left & right & 1) != 1:
        shift += 1
        left = left >> 1
        right = right >> 1 
    return left << shift


#---------------------------------------------------------------------------------
# 方法三：暴力

def rangeBitwiseAnd3(left, right):
    res = left 
    cur = left + 1
    while cur <= right:
        res &= cur
        cur += 1
    return res


#---------------------------------------------------------------------------------

def main():   
    a = 0b11001001
    b = 0b11010000
    print(rangeBitwiseAnd1(a, b))
    print(rangeBitwiseAnd2(a, b))
    print(rangeBitwiseAnd3(a, b))

if __name__ == "__main__":
    main()   