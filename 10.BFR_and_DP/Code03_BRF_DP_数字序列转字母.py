###########################################################################
# 1 - > a
# 26  -> bf or z
# input: a number str
# output: how may character strs could be converted 
###########################################################################



#暴力递归一
def countOfNumsToChars(str):
    if not str or len(str)==0:
        return 0
    return process(str,0)

def process(str, i):
    if i == len(str):
        return 1
    # if i > len(str):    #也可以在下边控制 i+1 < len(str)
    #     return 0

    if str[i] == "0":
        return 0
    elif str[i] == "1":
        cnt = process(str, i+1)
        if i+1 < len(str):
            cnt += process(str, i+2)
    elif str[i] == "2":
        cnt = process(str, i+1)
        if i+1 < len(str) and str[i+1] != '7' and str[i+1] != '8' and str[i+1] != '9':
            cnt += process(str, i+2)
    else:
        cnt = process(str, i+1)
    return cnt


#暴力递归二， 优化判断数字
def countOfNumsToChars2(str):
    if not str or len(str)==0:
        return 0
    return process(str,0)

def process2(str, i):
    if i == len(str):
        return 1
    if str[i] == "0":
        return 0
    cnt = process2(str, i+1)
    if i+1<len(str) and int(str[i])*10 + int(str[i+1]) < 27:
        cnt += process2(str, i+2)
    return cnt


#------------------------------------------------------------------------
#动态规划

def countOfNumsToChars3(str):
    if not str or len(str)==0:
        return 0
    n = len(str)
    dp = [0]*(n+1)
    dp[n] = 1
  
    for i in range(n-1, -1, -1):
        if str[i] != "0":
            dp[i] = dp[i+1]
            if i+1<n and (int(str[i]))*10 + (int(str[i+1])) < 27:
                dp[i] += dp[i+2]
    return dp[0]



#------------------------------------------------------------------------
def main():
    str = '1211235'
    #str = "121"
    print(countOfNumsToChars(str))
    print(countOfNumsToChars2(str))
    print(countOfNumsToChars3(str))

if __name__ == "__main__":
    main()