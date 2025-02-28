###########################################################################
# (从左往右， 选与不选)
#   打印一个字符串的全部排列， 要求不要出现重复的排列
###########################################################################


# 打印一个字符串的全部排列， 要求不要出现重复的排列
#   方法一： 用set， 在放入结果res时去重
def NoDupPermutations(str):
    if not str or len(str)==0:
        return 
    char_lst = list(str)
    res = set()
    f4(char_lst, 0, res)
    return list(res)

def f4(char_lst, i, res):
    if i == len(char_lst):
        res.add("".join(char_lst))
    else:
        for j in range(i, len(char_lst)):
            char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
            f4(char_lst, i+1, res)
            char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
 


#   方法二：  优化。 在交换时避免重复放入相同字符
def NoDupPermutations2(str):
    if not str or len(str)==0:
        return 
    char_lst = list(str)
    res =[]
    f5(char_lst, 0, res)
    return res

def f5(char_lst, i, res):
    if i == len(char_lst):
        res.append("".join(char_lst))
    else:
        s = set()
        for j in range(i, len(char_lst)):
            if char_lst[j] not in s:
                s.add(char_lst[j])
                char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
                f5(char_lst, i+1, res)
                char_lst[i], char_lst[j] = char_lst[j], char_lst[i]



#---------------------------------------------------------------------------
def main():

    str = "acc"
    print(NoDupPermutations(str)) 
    # # ['cca', 'acc', 'cac']
    str = "acc"
    print(NoDupPermutations2(str)) 


if __name__ == "__main__":
    main()