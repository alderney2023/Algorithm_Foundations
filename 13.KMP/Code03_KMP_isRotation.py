



def isRotation(s1,s2):
    if not s1 or not s2 or len(s1) != len(s2):
        return False
    return kmp(s1+s1, s2) != -1

def kmp(s1,s2):
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
        return -1
    
def nextArr(s):
    m = len(s)
    if m == 1:
        return [-1]
    next = [0] * m
    next[0] = -1
    next[1] = 0
    i = 2 
    cn = 0
    while i < m:
        if s[i-1] == s[cn]:
            next[i] = cn+1
            i += 1
            cn += 1
        elif cn == 0:
            next[i] = 0 
            i += 1
        else:
            cn = next[cn]
    return next


#--------------------------------------------------------------------------

def main():

    s1 = "taowang"
    s2 = "wangtao"

    print(isRotation(s1,s2))


if __name__ == "__main__":
    main()
    