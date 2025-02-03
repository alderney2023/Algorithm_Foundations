###########################################################################
#   数组中每一个值代表钱的一张货币，每张货币只能拿一次或者不拿，
#   凑够一个指定的数额，问有多少种凑法。
#
#   暴力递归
#   动态规划
###########################################################################

import random

#---------------------------------------------------------------------------------
#暴力递归

def ways1(choices, target):
    if not choices or len(choices)==0:
        return 0
    return process(choices, 0, target)

def process(choices, i, rest):
    if rest < 0:
        return 0
    if i == len(choices):
        if rest == 0:
            return 1
        else:
            return 0
    return process(choices, i+1, rest) + process(choices, i+1, rest-choices[i])
        

#---------------------------------------------------------------------------------
#动态规划

def ways2(choices, target):
    if not choices or len(choices)==0:
        return 0
    dp = [ [0] * (target+1) for _ in range(len(choices) + 1) ]
    dp[len(choices)][0] = 1
    for j in range(1,len(choices)+1):
        dp[len(choices)][j] = 0
    for i in range(len(choices)-1, -1 , -1):
        for rest in range(target+1):
            if rest-choices[i] >= 0:
                dp[i][rest] = dp[i+1][rest] + dp[i+1][rest-choices[i]]
            else:
                dp[i][rest] = dp[i+1][rest] + 0 
    return dp[0][target]



#---------------------------------------------------------------------------------

def generateRandomNumList(max_number, size):
    lst = []
    for i in range(size):
        x = int(random.random() * max_number) + 1
        lst.append(x)
    return lst


def main():
    #choices = [2,3,5,10,20]
    max_number = 5
    size = 10
    choices = generateRandomNumList(max_number, size)
    target = 20

    print(choices, target)
    print(ways1(choices, target))
    print(ways2(choices, target))

if __name__ == "__main__":
    main()