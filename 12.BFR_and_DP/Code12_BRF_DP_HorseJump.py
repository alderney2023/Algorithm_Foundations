
###########################################################################
# 棋盘大小为10 * 9
# 当前位置是（0，0）
# 还剩下rest步需要跳
# 跳完rest步，正好跳到a，b的方法数是多少？
###########################################################################



#---------------------------------------------------------------------------------
#暴力递归

def jump(a, b, steps):
    if a>9 or a<0 or b>8 or b<0:
        return 0
    return process(a, b, 0, 0, steps)

def process(a, b, x, y, rest):  
    if x>9 or x<0 or y>8 or y<0:
        return 0
    if rest == 0:
        if x == a and y == b:
            return 1
        else:
            return 0
    return process(a, b, x+1, y+2, rest-1) + \
            process(a, b, x+1, y-2, rest-1) + \
            process(a, b, x-1, y+2, rest-1) + \
            process(a, b, x-1, y-2, rest-1) + \
            process(a, b, x+2, y+1, rest-1) + \
            process(a, b, x+2, y-1, rest-1) + \
            process(a, b, x-2, y+1, rest-1) + \
            process(a, b, x-2, y-1, rest-1) 
    

#---------------------------------------------------------------------------------
#动态规划

def jump2(a, b, steps):
    if a>9 or a<0 or b>8 or b<0:
        return 0
    
    dp = [ [ [0]*(steps+1) for _ in range(9) ] for _ in range(10) ] 
    dp[a][b][0] = 1
    for rest in range(1, steps+1):
        for x in range(10):
            for y in range(9):
                dp[x][y][rest] = getValue(dp, x+1 , y+2, rest-1) + \
                                getValue(dp, x+1, y-2, rest-1) + \
                                getValue(dp, x-1, y+2, rest-1) + \
                                getValue(dp, x-1, y-2, rest-1) + \
                                getValue(dp, x+2, y+1, rest-1) + \
                                getValue(dp, x+2, y-1, rest-1) + \
                                getValue(dp, x-2, y+1, rest-1) + \
                                getValue(dp, x-2, y-1, rest-1) 
    return dp[0][0][steps]


def getValue(dp, x, y, rest):
	if (x < 0 or x > 9 or y < 0 or y > 8):
		return 0
	return dp[x][y][rest]



#---------------------------------------------------------------------------------

def main():
    a = 7
    b = 7
    steps = 10
    print(jump(a, b, steps))
    print(jump2(a, b, steps))


if __name__ == "__main__":
    main()