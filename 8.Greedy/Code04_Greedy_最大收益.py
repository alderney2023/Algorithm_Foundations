###########################################################################
# 输入：正数数组cost, 正数数组profits， 正数K， 正数M
# costs[i]: i号项目的花费
# profits[i]: i号项目的利润
# K：最多可以做K个项目
# M：初始资金
# 每做完一个项目，马上获得本金和收益，可以支持做下一个项目，不能并行做项目
# 输出：最后获得的最大钱数（包括本金和收益）
###########################################################################

import heapq

#贪心算法

class Program:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit

def maxEarning(costs, profits, K, M):
    programs = [ Program(costs[i], profits[i]) for i in range(len(costs)) ]

    cost_minheap = []  #   (cost, program)
    for p in programs:
        heapq.heappush(cost_minheap, (p.cost, p) )

    profit_maxheap = []  # (-profit, program)
    for i in range(K):
        while cost_minheap and cost_minheap[0][0] <= M:
            x = heapq.heappop(cost_minheap)
            heapq.heappush(profit_maxheap, (-x[1].profit, x[1]) )
        
        if profit_maxheap:
            x = heapq.heappop(profit_maxheap)
            M += (-x[0])
        else:
            return M
    return M


#---------------------------------------------------------------------------------

def main():
    costs = [20,1,4,7,15]
    profits = [10,3,4,6,7]
    K= 3
    M = 1
    print(maxEarning(costs, profits, K, M))


if __name__ == "__main__":
    main()