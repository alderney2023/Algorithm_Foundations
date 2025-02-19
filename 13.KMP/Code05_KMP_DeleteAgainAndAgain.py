############################################################################
# 不停删除之后剩下的字符串
# 给定一个字符串s1，如果其中含有s2字符串，就删除最左出现的那个
# 删除之后s1剩下的字符重新拼接在一起，再删除最左出现的那个
# 如此周而复始，返回最终剩下的字符串
#
# 测试链接 : https://www.luogu.com.cn/problem/P4824
############################################################################


def kmp_similar(s1,s2):
    n = len(s1)
    m = len(s2)
    next = nextArr(s2)

    stack1, stack2 = [], []
    x, y, size = 0, 0, 0
    while x < n :          ###
        if s1[x] == s2[y]:
            stack1.append(x)
            stack2.append(y)
            size += 1
            x += 1
            y += 1
        elif y == 0:
            stack1.append(x)
            stack2.append(-1)
            size += 1
            x += 1
        else:
            y = next[y]
        if y == m:
            for i in range(m):
                size -= 1
                stack1.pop()
                stack2.pop()
            if size > 0:
                y = stack2[-1] + 1
            else:
                y = 0
    s = ""
    for i in stack1:
        s += s1[i]
    return s

def nextArr(s):
    m = len(s)
    if m == 1:
        return [-1]
    next = [0] * m
    next[0] = -1
    next[1] = 0 
    #i表示当前要求next值的位置
	#cn表示当前要和前一个字符比对的下标
    i = 2
    cn = 0 
    while i < m:
        if s[i-1] == s[cn]:
            next[i] = cn + 1
            cn += 1
            i += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[i] = 0
            i += 1
    return next


#--------------------------------------------------------------------------

def main():

    s1 = "whatthemomooofun"
    s2 = "moo"
    #print(nextArr(s1))
    res = kmp_similar(s1, s2)
    print(res)


if __name__ == "__main__":
    main()
    