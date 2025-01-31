###########################################################################
#   最短路径   Dijkstra算法   
#     前提： 规定出发点，没有权重为负数的边
#     方法： 借用一个dictionary，一个set
#     思想： 字典中存储当前可以走到的节点及当前从起始点到这个点的距离，
#           选择一个最短路径往下走一步，走过的节点锁住，更新距离，再往下选下一个最短路径...
###########################################################################



def dijkstra(start):
    res = {}   # 存储节点和距离对 {node:distance}
    res[start] = 0
    selectedNodes = set()  #处理过的最短距离节点
    minNode = getMinDistanceAndUnselectedNode(res, selectedNodes)
    while minNode:
        distance = res.get(minNode)
        for edge in minNode.edges:
            next_node = edge.to
            if next_node not in selectedNodes:
                res[next_node] = distance + edge.weight
            else:
                res[next_node] = min( res.get(next_node), distance + edge.weight )
        #加入set， 选择下一个
        selectedNodes.add(minNode)
        minNode = getMinDistanceAndUnselectedNode(res, selectedNodes)
    return res


def getMinDistanceAndUnselectedNode(distanceMap, selectedNodes):
    min_distance = float('inf') 
    minNode = None
    for node,distance in distanceMap.items():
        if node not in selectedNodes and distance < min_distance:
            minNode = node
            min_distance = distance
    return minNode


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
    dic = dijkstra(graph.nodes.get(0))
    print(dic)

if __name__ == "__main__":
    main()