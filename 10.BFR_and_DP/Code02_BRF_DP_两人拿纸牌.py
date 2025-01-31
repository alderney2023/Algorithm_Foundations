###########################################################################
# 一个数组代表数值不同的纸牌排成一条线
# 两个玩家A和B依次拿纸牌， 只能从最左或最右取牌
# A先拿，B后拿， 假定两人绝顶聪明
# 返回赢家最后获胜的分数
###########################################################################


import random


#---------------------------------------------------------------------------------
#暴力递归 

def win1(cards):
    if not cards or len(cards)==0:
        return 
    n = len(cards)
    return max( first(cards, 0, n-1), second(cards, 0, n-1) )

def first(cards, L, R):
    if L==R:
        return cards[L]
    return max( cards[L] + second(cards, L+1, R), cards[R] + second(cards, L, R-1))

def second(cards, L, R):
    if L==R:
        return 0
    return min( first(cards, L+1, R), first(cards, L, R-1))


# #---------------------------------------------------------------------------------
# #动态规划

def win2(cards):
    if not cards or len(cards)==0:
        return 
    n = len(cards)

    dp_first = [ [0]*n for _ in range(n)]
    dp_second = [ [0]*n for _ in range(n)]
    for i in range(n):
        dp_first[i][i] = cards[i]
    ## dp_first[i][i] = 0
    for t in range(1,n):
        i ,j = 0, t
        while j<n:
            dp_first[i][j] = max( cards[i] + dp_second[i+1][j] , cards[j] + dp_second[i][j-1] )
            dp_second[i][j] = min( dp_first[i+1][j] , dp_first[i][j-1] )
            i+=1
            j+=1

    # 另一种循环方式
    # for i in range(n-2,-1,-1):
    #     for j in range(i+1,n):
    #         print(i,j)
    #         dp_first[i][j] = max( cards[i] + dp_second[i+1][j] , cards[j] + dp_second[i][j-1] )
    #         dp_second[i][j] = min( dp_first[i+1][j] , dp_first[i][j-1] )



    return max( dp_first[0][n-1], dp_second[0][n-1] )


#---------------------------------------------------------------------------------

def generaterandomlistwithoutdup(number,maxvalue):
    lst = []
    i = 0
    while i < number:
        x = int(random.random()*maxvalue) + 1
        if x not in lst:
            lst.append(x)
            i+=1
    return lst

def main():
    cards = generaterandomlistwithoutdup(4, 20)
    print(cards)
    print(win1(cards))
    print(win2(cards))

if __name__ == "__main__":
    main()