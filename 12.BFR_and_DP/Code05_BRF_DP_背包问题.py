###########################################################################
# 两个列表，一个代表每件货物的重量，一个代表每件货物的价值
# 求在给定最大重量W的情况下可以获得的最大价值
###########################################################################

import random 

#---------------------------------------------------------------------------------
#暴力递归

def getMaxValue(weight_list, value_list, max_weight):
    if (not weight_list) or len(weight_list)==0 \
        or (not value_list) or len(value_list)==0 \
        or max_weight<=0:
        return 0
    return process(weight_list, value_list, 0, max_weight)

def process(weight_list, value_list, i, rest_weight) :
    if i == len(weight_list):
        return 0
    no = process(weight_list, value_list, i+1, rest_weight) 
    yes = 0
    if rest_weight - weight_list[i] >= 0:
        yes = value_list[i] + process(weight_list, value_list, i+1, rest_weight - weight_list[i]) 
    return max(yes, no)



#------------------------------------------------------------------------
#动态规划

def getMaxValue2(weight_list, value_list, max_weight):
    if (not weight_list) or len(weight_list)==0 \
        or (not value_list) or len(value_list)==0 \
        or max_weight<=0:
        return 0
    n = len(weight_list)
    dp = [ [0] * (max_weight+1) for _ in range(n+1) ]
    for i in range(n-1,-1,-1):
        for j in range(max_weight+1):
            no = dp[i+1][j] 
            yes = 0
            if j - weight_list[i] >= 0:
                yes = value_list[i] + dp[i+1][j - weight_list[i]]
            dp[i][j]= max(yes, no)
    return dp[0][max_weight] 



#------------------------------------------------------------------------

def generateRandomNumList(max_number, size):
    lst = []
    for i in range(size):
        x = int(random.random() * max_number) + 1
        lst.append(x)
    return lst

def main():
    # weight_list = [10,15,20,30,35,40,10,5]
    # value_list = [2,4,8,6,2,6,10,8]
    # # weight_list = [8,10,20,10]  
    # # value_list = [20,10,8,100]
    # max_weight = 30

    weight_list = generateRandomNumList(10, 5)
    value_list = generateRandomNumList(5, 5)
    max_weight = 10

    print("weight:", weight_list)
    print("values:",value_list)
    print(getMaxValue(weight_list, value_list, max_weight))
    print(getMaxValue2(weight_list, value_list, max_weight))



if __name__ == "__main__":
    main()