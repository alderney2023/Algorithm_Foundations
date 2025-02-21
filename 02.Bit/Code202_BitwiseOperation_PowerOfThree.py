#############################################################################
# 判断一个整数是不是3的幂
#
# 测试链接 : https://leetcode.cn/problems/power-of-three/
#############################################################################


def max_power_of_three():
    max_limit = 2**31 - 1  # 32 位有符号整数的最大值
    power = 1  # 3^0 = 1
    while power * 3 <= max_limit:
        power *= 3  
    return power

def powerOfThree(n):
    return n > 0 and max_power_of_three() % n == 0



def main():   
    
    print(powerOfThree(9))
    print(powerOfThree(81))
    print(powerOfThree(100))

if __name__ == "__main__":
    main()   