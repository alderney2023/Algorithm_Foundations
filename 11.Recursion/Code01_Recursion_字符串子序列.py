###########################################################################
# (从左往右， 选与不选)
#  打印一个字符串的全部子序列    

###########################################################################

# 打印一个字符串的全部子序列  
def SubSequences(str):
    if not str or len(str)==0:
        return 
    res = []
    s = ""
    return f1(str, 0, s, res)

# str: 不变，i: 走到的位置， s: 目前选的字符，res：最终结果
def f1(str, i, s, res):
    if i == len(str):
        res.append(s)
        return
    f1(str, i+1, s+str[i], res)
    f1(str, i+1 ,s, res)
    return res



#---------------------------------------------------------------------------
def main():
    str = "abc"
    print(SubSequences(str))
    # ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']


if __name__ == "__main__":
    main()