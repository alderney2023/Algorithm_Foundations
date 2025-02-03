###########################################################################
#   最小生成树   Prim算法   
#     前提： 无向图
#     方法： 借用一个heap(小根堆)， 一个set
#     思想： 走到的点放入set， 并解锁可到达的边放入小根堆，
#           每个堆顶的边并且通向一个未到达过的点，此边可入结果集
###########################################################################

import heapq

def primMST(graph):
    node_set = set()  # 存贮已经走到的节点
    edge_heap = []     #存储解锁的边
    res = []        # 存储返回的结果
    for node in graph.nodes.values(): ## 从一个点开始， 也为了避免森林
        if node not in set:
            node_set.add(node)
            for edge in node.edges:
                heapq.heappush(edge_heap, edge)
            while edge_heap:
                edge = heapq.heappop(edge_heap)
                next_node = edge.to
                if next_node not in node_set:
                    res.append(edge)
                    node_set.add(next_node)
                    for edge in next_node.edges:
                        heapq.heappush(edge_heap, edge)
        return res



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
    lst = primMST(graph)
    print( [edge.weight for edge in lst] )

if __name__ == "__main__":
    main()