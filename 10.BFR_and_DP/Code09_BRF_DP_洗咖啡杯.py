###############################################################################################
# 认为每个人喝咖啡的时间非常短，冲好的时间即是喝完的时间。
# 每个人喝完之后咖啡杯可以选择洗或者自然挥发干净，只有一台洗咖啡杯的机器，只能串行的洗咖啡杯。
# 洗杯子的机器洗完一个杯子时间为a，任何一个杯子自然挥发干净的时间为b。
# 四个参数：arr, n, a, b
# 假设时间点从0开始，返回所有人喝完咖啡并洗完咖啡杯的全部过程结束后，至少来到什么时间点。
###############################################################################################

import random

#---------------------------------------------------------------------------------
# 暴力递归

def bestTime1(drinks, a, b):
    if not drinks or len(drinks)==0:
        return 0 
    return process1(drinks, a, b, 0, 0, 0)

def process1(drinks, a, b, i, machineFree, time):
    if i == len(drinks):
        return time

    wash = max(drinks[i], machineFree) + a
    t1 = process1(drinks, a, b, i+1, wash, max(wash, machineFree))
    dry = drinks[i] + b
    t2 = process1(drinks, a, b, i+1, machineFree, max(dry, machineFree))
    return min(t1, t2)
    

#---------------------------------------------------------------------------------
# 贪心+暴力

def bestTime2(drinks, a, b):
    if not drinks or len(drinks)==0:
        return 0 
    return process2(drinks, a, b, 0, 0)

def process2(drinks, a, b, i, machineFree):
    if i == len(drinks) - 1:
        wash = max(drinks[i], machineFree) + a
        dry = drinks[i] + b
        return min(wash, dry)
    
    cur_wash = max(drinks[i], machineFree) + a
    nexts_wash = process2(drinks, a, b, i+1, cur_wash)
    p1 = max(cur_wash, nexts_wash)
    cur_dry = drinks[i] + b
    nexts_dry = process2(drinks, a, b, i+1, machineFree)
    p2 = max(cur_dry, nexts_dry)
    return min(p1,p2)

#---------------------------------------------------------------------------------
#动态规划

def bestTime3(drinks, a, b):
    if not drinks or len(drinks)==0:
        return 0 
    
    machineFree = 0 
    for i in range(len(drinks)):
        machineFree += ( max(drinks[i],machineFree) + a )
    #print("machineFree:",machineFree)
    
    dp = [ [0] * machineFree for _ in range(len(drinks)) ]

    for j in range(machineFree):
        wash = max(drinks[len(drinks)-1], j) + a
        dry = drinks[len(drinks)-1] + b
        dp[len(drinks)-1][j] =  min(wash, dry)

    for i in range(len(drinks)-2, -1, -1):
        for j in range(machineFree):
            cur_wash = max(drinks[i], j) + a
            #print("**", i+1, cur_wash)
            if cur_wash < machineFree:
                nexts_wash = dp[i+1][cur_wash]
            p1 = max(cur_wash, nexts_wash)
            cur_dry = drinks[i] + b
            nexts_dry = dp[i+1][j]
            p2 = max(cur_dry, nexts_dry)
            dp[i][j] = min(p1,p2)

    return dp[0][0]



#---------------------------------------------------------------------------------

def generateRandomList(size,maxvalue):
    lst = []
    for i in range(size):
        x = int(random.random()*maxvalue) + 1
        lst.append(x)
    return lst

def main():
    #drinks = [1,1,2,10]
    drinks = sorted(generateRandomList(10,50))
    a = 3
    b = 10
    print(bestTime1(drinks, a, b))
    print(bestTime2(drinks, a, b))
    print(bestTime3(drinks, a, b))

if __name__ == "__main__":
    main()