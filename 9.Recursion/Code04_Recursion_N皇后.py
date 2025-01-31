

#递归 方法一
def NQueen(n):
    if n<1:
        return 0
    record = [0] * n
    return process(n, 0, record)

def process(n, row, record):
    if row == n:
        return 1
    cnt = 0
    for col in range(n):
        if isValid(row, col, record):
            record[row] = col
            cnt += process(n, row+1, record)
    return cnt

def isValid(row,col,record):
    for t in range(row):
        if col == record[t] or abs(row-t) == abs(col-record[t]):
            return False
    return True


#---------------------------------------------------------------------------------
#递归 方法二 位运算替代数组

def NQueen2(n):
    if n<1:
        return 0
    limit = (1 << n) - 1
    col_lim = 0
    left_diag_lim = 0
    right_diag_lim = 0
    return process2(limit, col_lim, left_diag_lim, right_diag_lim)

def process2(limit, col_lim, left_diag_lim, right_diag_lim):
    if col_lim == limit:
        return 1
    res = 0
    # 还可以放的位为1
    pos = limit & (~(col_lim | left_diag_lim | right_diag_lim))
    while pos:  
        mostRightOne = pos & (~pos + 1)
        res += process2(limit, \
                col_lim | mostRightOne,
                (left_diag_lim | mostRightOne) << 1, \
                (right_diag_lim | mostRightOne) >> 1)
        pos = pos ^ mostRightOne
    return res



#---------------------------------------------------------------------------------

def main():
    print(NQueen(4))
    print(NQueen2(4))

if __name__ == "__main__":
    main()