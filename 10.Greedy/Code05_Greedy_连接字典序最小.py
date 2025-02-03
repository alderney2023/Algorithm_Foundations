
###########################################################################
#   一个数组包括很多字符串，将这些字符串都拼接起来成为一个大的字符串，如何拼接可以使得这个字符串的字典序最小
###########################################################################

#贪心算法

from functools import cmp_to_key

def compare(a,b):
    if a+b < b+a:
        return -1
    else:
        return 1

def minDic(lst):
    newlst = sorted(lst, key = cmp_to_key(compare)) 
    print(newlst)
    res = ""
    for x in newlst:
        res += x
    return res


#---------------------------------------------------------------------------------

def main():
    lst = ["a","abc","abd","aa","bd"]
    print(lst)
    print(minDic(lst))


if __name__ == "__main__":
    main()