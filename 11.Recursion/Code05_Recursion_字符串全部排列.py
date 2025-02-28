###########################################################################
# (从左往右， 选与不选)
#   打印一个字符串的全部排列
###########################################################################

# 打印一个字符串的全部排列
def Permutations(str):
    if not str or len(str)==0:
        return 
    char_lst = list(str)
    res = []
    return f3(char_lst, 0, res)

def f3(char_lst, i, res):
    if i == len(char_lst):
        res.append("".join(char_lst))
        return
    for j in range(i, len(char_lst)):
        char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
        f3(char_lst, i+1, res)
        char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
    return res



#---------------------------------------------------------------------------
def main():

    str = "abc"
    print(Permutations(str)) 
    # # ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']

if __name__ == "__main__":
    main()