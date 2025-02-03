###########################################################################
#   数组中每一个值代表钱的一张货币，每张货币只能拿一次或者不拿，
#   凑够一个指定的数额，问最少用多少张
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
        return -1
    if rest == 0:
        return 0
    if i == len(choices):
        return -1

    no = yes = -1
    no = process(choices, i+1, rest)
    yes = process(choices, i+1, rest - choices[i])

    if yes == -1 and no == -1:
        return -1
    elif yes == -1:
        return no
    elif no == -1:
        return yes+1
    else:
        return min(1+yes, no)


#---------------------------------------------------------------------------------
#动态规划

def ways2(choices, target):
    if not choices or len(choices)==0:
        return 0

    dp = [ [-1]*(target+1) for _ in range(len(choices) + 1) ]
    for i in range(len(choices)+1):
        dp[i][0] = 0
    for rest in range(1, target+1):
        dp[len(choices)][rest] = -1

    for i in range(len(choices)-1, -1, -1):
        for rest in range(1, target+1):
            no = yes = -1
            no = dp[i+1][rest]
            yes = dp[i+1][rest - choices[i]]

            if yes == -1 and no == -1:
                dp[i][rest] = -1
            elif yes == -1:
                dp[i][rest] = no
            elif no == -1:
                dp[i][rest] = yes+1
            else:
                dp[i][rest] = min(1+yes, no)
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
    target = 10

    print(choices, target)
    print(ways1(choices, target))
    print(ways2(choices, target))

if __name__ == "__main__":
    main()