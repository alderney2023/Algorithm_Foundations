###########################################################################
#   最小生成树   Kruskal算法   
#     前提： 无向图
#     方法： 借用一个heap(小根堆), 一个UnionSet, 出heap打印
#     思想： 开始每个点各自一个集合，每次选择一个最短边，把两边点合并为一个集合，
#            当所有点在同一个集合即完成
#   def kruskalMST(graph)
#   class UnionSet
#   class Node
#   class Edge
#   class Graph
#   def createGraph(lst)
###########################################################################

import heapq

def kruskalMST(graph):
    # 堆， 存贮边
    edge_heap = []
    for edge in graph.edges:
         heapq.heappush(edge_heap, edge)
    # 并查集， 存储节点
    us = UnionSet(graph.nodes.values())  # graph.nodes = {value:node} 所以要values()入堆
    
    res = []
    while edge_heap:
        edge = heapq.heappop(edge_heap)
        if not us.isSameSet(edge.source, edge.to):  # edge.weight 要重载 < 运算符
            us.union(edge.source, edge.to)
            res.append(edge)
    return res
    
#---------------------------------------------------------------------------------

class UnionSet:

    def __init__(self, values):
        self.father = {}
        self.sizeMap = {}
        for v in values:
            self.father[v] = v
            self.sizeMap[v] = 1   #只有每个set的头节点才存在于sizeMap
    

    def findFather(self, v):
        stack = []
        while self.father.get(v) != v:
            stack.append(v)
            v = self.father.get(v)
        while stack:
            self.father[stack.pop()] = v
        return v


    def isSameSet(self, v1, v2):
        if (v1 not in self.father) or (v2 not in self.father):
            return False 
        return self.findFather(v1) == self.findFather(v2)


    def union(self, v1, v2):
        if (v1 not in self.father) or (v2 not in self.father) or (self.isSameSet(v1,v2)):
            return 
        a = self.findFather(v1)
        b = self.findFather(v2)
        if self.sizeMap[a] >= self.sizeMap[b]:
            large, small = a, b
        else:
            large, small = b, a
        self.father[small] = large
        self.sizeMap[large] += self.sizeMap[small]
        del self.sizeMap[small]

    def sets(self):
        return len(self.sizeMap)

#---------------------------------------------------------------------------------

class Node:
    def __init__(self,value=0, in_cnt=0, out_cnt=0, nexts=None, edges=None):
        self.value = value
        self.in_cnt = in_cnt
        self.out_cnt = out_cnt
        self.nexts = nexts if nexts is not None else []
        self.edges = edges if edges is not None else []


class Edge:
    def __init__(self, weight=0, source=None, to=None):
        self.weight = weight
        self.source = source
        self.to = to

    def __lt__(self, other):
        # 比较两个Edge对象的权重
        return self.weight < other.weight


class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes if nodes is not None else {}
        self.edges = edges if edges is not None else set()


def createGraph(lst):
    graph = Graph()
    for x in lst:
        edgeW, sourceV, toV = x[0], x[1], x[2]
        if not graph.nodes.get(sourceV):
            graph.nodes[sourceV] = Node(sourceV)     
        if not graph.nodes.get(toV):
            graph.nodes[toV] = Node(toV)
        n1 = graph.nodes.get(sourceV)
        n2= graph.nodes.get(toV)
        n1.out_cnt += 1
        n2.in_cnt += 1
        n1.nexts.append(n2)
        e = Edge(edgeW, n1, n2)
        n1.edges.append(e)
        graph.edges.add(e)
    return graph



#---------------------------------------------------------------------------------

def main():
    g = [ [ 5 , 0 , 2],[ 5 , 2 , 0],
          [ 3 , 0,  1],[ 3 , 1,  0],
          [ 10, 1,  4],[ 10, 4,  1],
          [ 8,  2,  3],[ 8,  3,  2],
          [ 2,  1,  3],[ 2,  3,  1] ]
    graph = createGraph(g)
    lst = kruskalMST(graph)
    print( [edge.weight for edge in lst] )

if __name__ == "__main__":
    main()