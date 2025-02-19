############################################################################
# 最短循环节的长度
# 给你一个字符串s，它一定是由某个循环节不断自我连接形成的
# 题目保证至少重复2次，但是最后一个循环节不一定完整
# 现在想知道s的最短循环节是多长
#
# 测试链接 : https://www.luogu.com.cn/problem/P4391
############################################################################

def RepeatMininmumLength(s):
    n = len(s)
    next = nextArr(s)
    return n - next[n]


def nextArr(s):
    m = len(s)
    if m == 1:
        return [-1]
    next = [0] * (m+1)
    next[0] = -1
    next[1] = 0
    i = 2 
    cn = 0
    while i <= m:
        if s[i-1] == s[cn]:
            next[i] = cn+1
            i+=1
            cn+=1
        elif cn == 0:
            next[i] = 0
            i+=1
        else:
            cn = next[cn]
    return next


#--------------------------------------------------------------------------

def main():

    s1 = "cabcabca"
    #print(nextArr(s1))
    print(RepeatMininmumLength(s1))


if __name__ == "__main__":
    main()
    