###########################################################################
#   数组中每一个值代表钱的一种面额，每种面额可以拿任意多次，凑够一个指定的数额，问有多少种凑法。
#
#   暴力递归
#   记忆化搜索
#   动态规划
#   动态优化 优化枚举
###########################################################################



#---------------------------------------------------------------------------------
#暴力递归

def ways1(choices,target):
    if not choices or len(choices)==0:
        return 0
    return process(choices, 0, target)

def process(choices, i, rest):
    # if rest == 0 :
    #     return 1
    # if i==len(choices):
    #     return 0 
    if i == len(choices):
        if rest == 0:
            return 1
        else:
            return 0
    res = 0
    for j in range( int(rest/choices[i])+1 ):
        res += process(choices, i+1, rest - choices[i] * j)
    return res


#---------------------------------------------------------------------------------
# 记忆化搜索

def ways2(choices,target):
    if not choices or len(choices)==0:
        return 0
    dp = [ [-1] * (target+1) for _ in range(len(choices)+1) ] 
    return process2(choices, 0, target, dp)

def process2(choices, i, rest, dp):
    if dp[i][rest] != -1:
        return dp[i][rest]
    if i == len(choices):
        if rest == 0:
            dp[i][0] = 1
            return dp[i][rest]
        else:
            dp[i][0] = 0
            return dp[i][rest]
    res = 0
    for j in range( int(rest/choices[i])+1 ):
        res +=  process(choices, i+1, rest - choices[i] * j)
    dp[i][rest] = res
    return dp[i][rest]


#---------------------------------------------------------------------------------
# 动态规划

def ways3(choices,target):
    if not choices or len(choices)==0:
        return 0
    dp = [ [0] * (target+1) for _ in range(len(choices)+1) ] 

    dp[len(choices)][0] = 1
    for i in range(len(choices)):
        dp[i][0] = 0

    for i in range(len(choices)-1,-1,-1):
        for rest in range(target+1):
            for j in range( int(rest/choices[i])+1 ):
                dp[i][rest] +=  dp[i+1][rest - choices[i] * j]
    return dp[0][target]


def ways4(choices,target):
    if not choices or len(choices)==0:
        return 0
    dp = [ [0] * (target+1) for _ in range(len(choices)+1) ] 

    dp[len(choices)][0] = 1
    for i in range(len(choices)):
        dp[i][0] = 0

    for i in range(len(choices)-1,-1,-1):
        for rest in range(target+1):
            dp[i][rest] = dp[i+1][rest] + dp[i][rest - choices[i]] 
    return dp[0][target]


#---------------------------------------------------------------------------------

def main():
    choices = [2,3,5,10,20]
    target = 20
    print(ways1(choices,target))
    print(ways2(choices,target))
    print(ways3(choices,target))
    print(ways4(choices,target))

if __name__ == "__main__":
    main()