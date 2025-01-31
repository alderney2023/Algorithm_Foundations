###########################################################################
# robot在一个范围内移动。 总共有road个位置，从start点出发，走steps步到达target
# robot每次走一步，在中间的位置可以往左也可以往右
# 如果走到1位置，下一步只能往右走到2，
# 如果走到最后一个位置，下一步只能往左走一个位置
# 求有多少种不同的走法
###########################################################################



#---------------------------------------------------------------------------------
#暴力递归

def robotWalk(road, start, target, steps):
    if (road < 2 or start < 1 or start > road or target < 1 or target > road or steps < 1):
        return -1
    return process(road, target, start, steps)

def process(road, target, cur_pos, rest_steps):
    if rest_steps == 0:
            return cur_pos == target
    if cur_pos == 1:
        return process(road, target, 2, rest_steps-1)
    elif cur_pos == road:
        return process(road, target, road-1, rest_steps-1)
    else:
        return process(road, target, cur_pos+1, rest_steps-1) + process(road, target, cur_pos-1, rest_steps-1)



#---------------------------------------------------------------------------------
# 记忆化搜索

def robotWalk2(road, start, target, steps):
    if road<2 or start<1 or start>road or target<1 or target>road or steps<1:
        return -1
    dp = [ [0] * (steps+1) for _ in range(road+1)]  #dp[cur][rest_steps]
    return process2(road, start, target, steps, dp)

def process2(road, target, cur_pos, rest_steps, dp):
    if rest_steps == 0:
        dp[cur_pos][rest_steps] = (cur_pos == target)
        return dp[cur_pos][rest_steps] 
    if cur_pos == 1:
        dp[cur_pos][rest_steps] = process(road, target, 2, rest_steps-1)
    elif cur_pos == road:
        dp[cur_pos][rest_steps] =process(road, target, road-1, rest_steps-1)
    else:
        dp[cur_pos][rest_steps] = process(road, target, cur_pos+1, rest_steps-1) + process(road, target, cur_pos-1, rest_steps-1)
    return dp[cur_pos][rest_steps]



#------------------------------------------------------------------------
#动态规划

def robotWalk3(road, start, target, steps):
    if (road < 2 or start < 1 or start > road or target < 1 or target > road or steps < 1):
        return -1
    #dp[cur_pos][rest_steps]
    dp = [ [0] * (road+1) for _ in range(road+1)]
    dp[target][0] = 1
    for j in range(1,steps+1): 
        dp[1][j] = dp[2][j-1]
        for i in range(2, road):
            dp[i][j] = dp[i+1][j-1] + dp[i-1][j-1]  
        dp[road][j] = dp[road][j-1]
    return dp[start][steps]
    

#---------------------------------------------------------------------------------

def main():
    road = 7
    start = 2
    target = 3
    steps = 5

    print(robotWalk(road,start,target,steps))
    print(robotWalk2(road,start,target,steps))
    print(robotWalk3(road,start,target,steps))

if __name__ == "__main__":
    main()