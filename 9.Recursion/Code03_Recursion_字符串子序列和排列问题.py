###########################################################################
# (从左往右， 选与不选)
#       1.打印一个字符串的全部子序列    
#       2.打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
# (从左往右， 当前字符与后边各位置字符交换)
#       3.打印一个字符串的全部排列
#       4.打印一个字符串的全部排列， 要求不要出现重复的排列
###########################################################################

# 1.打印一个字符串的全部子序列  
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
# 2. 打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
def NoDupSubSequences(str):
    if not str or len(str)==0:
        return 
    res = set()
    s = ""
    return f2(str, 0, s, res)

def f2(str, i, s, res):
    if i == len(str):
        res.add(s)
        return
    f2(str, i+1, s+str[i], res)
    f2(str, i+1, s, res)
    return res


#---------------------------------------------------------------------------
# 3.打印一个字符串的全部排列
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
# 4.打印一个字符串的全部排列， 要求不要出现重复的排列
#   方法一： 用set， 在放入结果res时去重
def NoDupPermutations(str):
    if not str or len(str)==0:
        return 
    char_lst = list(str)
    res = set()
    return f4(char_lst, 0, res)

def f4(char_lst, i, res):
    if i == len(char_lst):
        res.add("".join(char_lst))
        return
    for j in range(i, len(char_lst)):
        char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
        f4(char_lst, i+1, res)
        char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
    return res    


#   方法二：  优化。 在交换时避免重复放入相同字符
def NoDupPermutations2(str):
    if not str or len(str)==0:
        return 
    char_lst = list(str)
    res = set()
    return f5(char_lst, 0, res)

def f5(char_lst, i, res):
    if i == len(char_lst):
        res.add("".join(char_lst))
        return
    s = set()
    for j in range(i, len(char_lst)):
        if char_lst[j] not in s:
            s.add(char_lst[j])
            char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
            f5(char_lst, i+1, res)
            char_lst[i], char_lst[j] = char_lst[j], char_lst[i]
    return res   


#---------------------------------------------------------------------------
def main():
    str = "abc"
    print(SubSequences(str))
    # ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']

    str = "acc"
    print(NoDupSubSequences(str))
    # ['', 'cc', 'ac', 'a', 'c', 'acc']

    str = "abc"
    print(Permutations(str)) 
    # # ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']

    str = "acc"
    print(NoDupPermutations(str)) 
    # # ['cca', 'acc', 'cac']
    str = "acc"
    print(NoDupPermutations2(str)) 


if __name__ == "__main__":
    main()