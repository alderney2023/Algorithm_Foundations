#############################################################################
# 判断一个整数是不是2的幂
#   方法：
#       Brian Kernighan算法
#       提取出二进制里最右侧的1

# 测试链接 : https://leetcode.cn/problems/power-of-two/
#############################################################################


def powerOfTwo(n):
    return n == (n & -n)


def main():   
    n=33
    print(powerOfTwo(n))


if __name__ == "__main__":
    main()   