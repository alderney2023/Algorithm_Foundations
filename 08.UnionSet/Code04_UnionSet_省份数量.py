
# https://leetcode.cn/problems/number-of-provinces/description/?envType=problem-list-v2&envId=union-find

#   方法一： 深度优先
#   方法二： 广度优先
#   方法三： 并查集



#---------------------------------------------------------------------------------
#深度优先
def findCircleNum1(isConnected):
    n = len(isConnected)
    help = [0] * n
    provinces = 0
    for i in range(n):
        if help[i] == 0:
            help[i] == 1 
            dfs(isConnected, n, i, help)
            provinces += 1
    return provinces

def dfs(isConnected, n, i, help):
    for j in range(n):
        if isConnected[i][j] == 1:
            help[j] = 1   
                

#---------------------------------------------------------------------------------
#广度优先
def findCircleNum2(isConnected):
    n = len(isConnected)
    help = [0] * n
    queue =[]
    provinces = 0
    for i in range(n):
        if help[i] == 0:
            queue.append(i)
            while queue:
                cur = queue.pop(0)
                help[cur] = 1 
                for j in range(n):
                    if isConnected[cur][j] == 1 and help[j] == 0:
                        queue.append(j)
            provinces += 1
    return provinces


#---------------------------------------------------------------------------------
#并查集

from Code01_UnionSet_灵活字典版 import UnionSet

def findCircleNum3(isConnected):
    n = len(isConnected)
    lst = [ i for i in range(n) ]
    us = UnionSet(lst)
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                us.union(i,j)
    return us.sets()





#---------------------------------------------------------------------------------

def main():
    isConnected1= [[1,1,0],[1,1,0],[0,0,1]]
    isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]

    print(findCircleNum1(isConnected1))
    print(findCircleNum1(isConnected2))

    print(findCircleNum2(isConnected1))
    print(findCircleNum2(isConnected2))

    print(findCircleNum3(isConnected1))
    print(findCircleNum3(isConnected2))


if __name__ == "__main__":
    main()