###########################################################################
#  给定一个字符串类型的数组arr 和 一个字符串word
#  arr里每一个字符串代表一张贴纸，你可以把单个字符剪开使用，目的是拼出str
#  返回需要至少多少张贴纸
#
#   本题测试链接：https://leetcode.com/problems/stickers-to-spell-word
#   hard
#
#   暴力递归
#   记忆化搜索  已是最优解
#
###########################################################################


#---------------------------------------------------------------------------------
#暴力递归

def minStickers1(arr, word):
    if not arr or len(arr)== 0 or word == "":
        return 0

    s = set()
    for sticker in arr:
        for c in sticker:
            s.add(c)
    t = set(word)
    for c in t:
        if c not in s:
            return -1

    return process1(arr, word)


def process1(arr, rest):
    if len(rest) == 0:
        return 0
    min_stickers = float('inf')
    for i in range(len(arr)):
        if rest[0] in arr[i]:
            min_stickers = min(min_stickers,  1 + process1(arr, AlphabetListMinus(rest, arr[i])))
    return min_stickers
    

def strToAlphabetList(s):
    alphabet = [0] * 26
    for c in s:
        alphabet[ord(c)-ord('a')] +=1
    return alphabet

def AlphabetListToStr(lst):
    res = ""
    for i in range(26):
        res += chr((ord('a')+i)) * lst[i]
    return res

def AlphabetListMinus(s1, s2):
    lst1 = strToAlphabetList(s1)
    lst2 = strToAlphabetList(s2)
    res = [0] * 26
    for i in range(26):
        res[i] = max( lst1[i] - lst2[i], 0) 
    return AlphabetListToStr(res)



#---------------------------------------------------------------------------------
# 记忆化搜索

def minStickers2(arr, word):
    if not arr or len(arr)== 0 or word == "":
        return 0

    s = set()
    for sticker in arr:
        for c in sticker:
            s.add(c)
    t = set(word)
    for c in t:
        if c not in s:
            return -1
    
    dic = {"":0}
    return process2(arr, word, dic)


def process2(arr, rest, dic):
    if rest in dic:
        return dic[rest]
    min_stickers = float('inf')
    for i in range(len(arr)):
        if rest[0] in arr[i]:
            min_stickers = min(min_stickers,  1 + process2(arr, AlphabetListMinus(rest, arr[i]), dic))
    dic[rest] = min_stickers
    return min_stickers


# 另一种方式处理 word中存在贴纸数组中没有的字母而无法拼凑成功的判断
def minStickers3(arr, word):
    if not arr or len(arr)== 0 or word == "":
        return 0
    dic = {"":0}
    ans = process3(arr, word, dic)
    if ans == float('inf'): 
        return -1
    else: 
        return ans

def process3(arr, rest, dic):
    if rest in dic:
        return dic[rest]  # 已将 rest =="": return 0 作为初始值赋给了dic

    min_stickers = float('inf')
    for i in range(len(arr)):
        if rest[0] in arr[i]:
            #min_stickers = min(min_stickers,  1 + process3(arr, AlphabetListMinus(rest, arr[i]), dic))
            min_stickers = min(min_stickers,  process3(arr, AlphabetListMinus(rest, arr[i]), dic))
    

    if min_stickers == float('inf'): #替代了在主函数中检查word中存在贴纸数组中没有的字母而无法拼凑成功的判断
        ans = min_stickers + 0
    else:
        ans = min_stickers + 1
    dic[rest] = ans
    return ans


#---------------------------------------------------------------------------------

def main():
    arr = ['ab','ccbd','aa','bb']
    word = 'abc'
    print(minStickers1(arr, word))
    print(minStickers2(arr, word))
    print(minStickers3(arr, word))  


    arr = ['ab','ccbd','aa','bb']
    word = 'abcx'
    print(minStickers1(arr, word))
    print(minStickers2(arr, word))
    print(minStickers3(arr, word))  



    
if __name__ == "__main__":
    main()