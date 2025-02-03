###########################################################################
#一块金条切成两半，是需要花费和长度一样的铜板的
#例如： 给定数组[10,20,30]，代表一共3个人，整条金条长度60，金条要分成10,20,30三个部分
#输入一个数组，返回分割的最小代价
###########################################################################
import heapq, random


#暴力递归
def cutGold(lst):
    if not lst or len(lst)==0:
        return 0
    res = []
    return process(lst)


def process(lst):
    if len(lst) == 1:
        return 0  
    min_total_cost = float('inf')  
    for i in range(len(lst)-1):
        for j in range(i + 1, len(lst)):
            cost = lst[i] + lst[j]
            new_lst = lst.copy()
            new_lst.pop(j)  
            new_lst.pop(i)
            new_lst.append(cost)  
            total_cost = cost + process(new_lst)
            min_total_cost = min(min_total_cost, total_cost)
    return min_total_cost


#---------------------------------------------------------------------------------
#贪心算法
def cutGold2(lst):
    if not lst or len(lst)==0:
        return 0
    heapq.heapify(lst)
    total_cost = 0
    while len(lst)>1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        cost = first + second
        total_cost+= cost
        heapq.heappush(lst, cost)
    return total_cost


#---------------------------------------------------------------------------------

def generateRandomList(maxValue, valueSize):
    lst = []
    for i in range(valueSize):
        x = int(random.random() * maxValue + 1)
        lst.append(x)
    return lst


def main():
    maxValue, valueSize = 20, 4
    lst = generateRandomList(maxValue, valueSize)
    print(lst)
    #lst = [10,20,30]

    print(cutGold(lst))
    print(cutGold2(lst))


if __name__ == "__main__":
    main()