#测试链接 : https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

def kmp(s1, s2):
    n = len(s1)
    m = len(s2)
    next = nextArr(s2)
    x, y = 0, 0 
    while x < n and y < m:
        if s1[x] == s2[y]:
            x += 1
            y += 1
        elif y == 0:
            x += 1
        else:
            y = next[y]
    if y == m:
        return x-y
    else:
        return-1


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

    s1 = "abxbacabybacabebacabzbac"
    s2 = "abebac"
    print(s1)
    print(s2)
    print(nextArr(s2))
    print(kmp(s1,s2))


if __name__ == "__main__":
    main()
    