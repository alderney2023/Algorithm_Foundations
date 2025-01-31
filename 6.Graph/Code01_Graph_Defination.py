
###########################################################################
#   图结构定义
#       class Node:    
#               value   值
#               in_cnt  入度
#               out_cnt 出度
#               nexts   指向的节点 list
#               edges   出去的边   list
#       class Edge:    
#               weight  权重
#               source  来自的Node
#               to      去向的Node
#       class Graph:    
#               nodes   所有节点    dictionary {value:Node} 
#               edges   所有边      set(Edge)
#       def createGraph(lst)  
#               包括（weight, source.value, to.value）的二维数组  --> 图
###########################################################################

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

def main():
    g = [ [ 5 , 0 , 2],
          [ 3 , 0,  1],
          [ 10, 1,  4],
          [ 8,  2,  3] ]
    graph = createGraph(g)
    
    for k,v in graph.nodes.items():
        print(k, end=" ")
    print()
    for x in graph.edges:
        print(x.weight, end=" ")
    print()

    for x in graph.nodes.get(0).nexts:
        print(x.value, end=" ")
    print()


if __name__ == "__main__":
    main()