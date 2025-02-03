###########################################################################
#   拓扑排序    
#     前提： 有向无环图
#     方法： 借用一个queue, 一个dictionary, 出queue打印
###########################################################################

from Code01_Graph_Defination import Node, Edge, Graph, createGraph

def TopologySort(g):
    zeroInQueue = []  #入度为0的节点
    inCntDic = {}   #{node:剩余入度}。入度为0可进queue; 进queue后的节点，它的每个下节点入度-1
    for node in g.nodes.values():
        inCntDic[node] = node.in_cnt
        if node.in_cnt == 0:
            zeroInQueue.append(node)
    res = []
    while zeroInQueue:
        cur = zeroInQueue.pop(0)
        res.append(cur)
        for next in cur.nexts:
            inCntDic[next] -= 1
            if inCntDic[next] == 0:
                zeroInQueue.append(next)
    return res
    

#---------------------------------------------------------------------------------

def main():
    g = [ [ 5 , 0 , 2],
          [ 3 , 0,  1],
          [ 10, 1,  4],
          [ 8,  2,  3],
          [ 2,  1,  3]]
    graph = createGraph(g)
    lst = TopologySort(graph)
    print( [node.value for node in lst] )

if __name__ == "__main__":
    main()