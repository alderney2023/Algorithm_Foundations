###########################################################################
# 在M*N的棋盘中，Bob的起始位置是a,b, 要走steps步，
# 如果走完后，Bob还在棋盘中就获得1个生存点，
# 问Bob的生存率
###########################################################################



#---------------------------------------------------------------------------------
#暴力递归


def livePosibility1(M, N, a, b, steps):
    all = 4 ** steps
    live = process(M, N, a, b, steps)
    return live / all


def process(M, N, x, y, rest):  # x,y 为当前位置，rest为还有多少步要走
    if x<0 or x>=M or y<0 or y>=N:
        return 0
    if rest == 0:
        return 1

    return process(M, N, x+1, y+1, rest-1) + \
            process(M, N, x+1, y-1, rest-1) + \
            process(M, N, x-1, y+1, rest-1) + \
            process(M, N, x-1, y-1, rest-1) 


#---------------------------------------------------------------------------------
#动态规划

def livePosibility2(M, N, a, b, steps):
    all = 4 ** steps

    dp = [ [ [0] * (steps+1) for _ in range(N) ] for _ in range(M) ]
    for x in range(M):
        for y in range(N):
            dp[x][y][0] = 1
    
    for rest in range(1, steps+1):
        for x in range(M):
            for y in range(N):
                dp[x][y][rest] = getValue(dp, M, N, x+1, y+1, rest-1) + \
                                getValue(dp, M, N, x+1, y-1, rest-1) + \
                                getValue(dp, M, N, x-1, y+1, rest-1) + \
                                getValue(dp, M, N, x-1, y-1, rest-1) 
    live = dp[a][b][steps]
    return live / all


def getValue(dp, M, N, x, y, rest):
	if (x < 0 or x >= M or y < 0 or y >= N):
		return 0
	return dp[x][y][rest]

#---------------------------------------------------------------------------------

def main():
    print( livePosibility1(50, 50, 6, 6, 10) )
    print( livePosibility2(50, 50, 6, 6, 10) )


if __name__ == "__main__":
    main()