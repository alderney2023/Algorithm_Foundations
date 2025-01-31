###########################################################################
#   最短路径   Dijkstra算法   
#     前提： 规定出发点，没有权重为负数的边
#     方法： 借用一个改写的minHeap(小根堆)，主要数据结构和逻辑都放在小根堆的内部函数中
#              小根堆里包括：
#                   主要数据结构 
#                       nodesHeap:      存储node的堆list    
#                       heapIndexDic:   存储node和对应堆位置的dictionary
#                       distanceDic:    存储node和到起始点的距离
#                       heapsize:       堆大小
#                   主要函数
#                        堆核心函数：
#                           _heapify
#                           _heapInsert
#                           size
#                           isEmpty
#                        堆改动定制函数
#                           addOrUpdateOrIgnore
#                           _isEntered，
#                           _inHeap， 
#                           _swap， 
#                           popRecord
###########################################################################

def dijkstra2(start):
    res = []
    heap = NodeMinHeap()
    heap.addOrUpdateOrIgnore(start, 0)
    while heap.size() :
        record = heap.popRecord()
        res.append(record)
        cur= record.node
        distance = record.distance
        for edge in cur.edges:
            heap.addOrUpdateOrIgnore(edge.to, edge.weight + distance )
    return res
        

#---------------------------------------------------------------------------------



class NodeRecord:
    def __init__(self, node, distance):
        self.node = node 
        self.distance = distance


class NodeMinHeap():

    def __init__(self, nodesHeap=None, heapIndexDic=None, distanceDic=None, heapsize=None):
        # 实际的堆结构
        self._nodesHeap = nodesHeap if nodesHeap is not None else []   
        # key 某一个node， value 上面堆中的位置
        self._heapIndexDic = heapIndexDic if heapIndexDic is not None else {} 
        # key 某一个节点， value 从源节点出发到该节点的目前最小距离
        self._distanceDic = distanceDic if distanceDic is not None else {} 
        # 堆上有多少个点
        self._heapsize = len(nodesHeap) if heapsize is not None else 0  
        # if self._nodesHeap:
        #     for i in range(self._heapsize):
        #         self._heapInsert(i)

    def _heapify(self, index):
        left = 2 * index + 1
        while left < self._heapsize:
            if left + 1 < self._heapsize and \
                self.distanceDic.get(self._nodesHeap[left+1]) < self.distanceDic.get(self._heap[left]):
                smallest = left+1
            else:
                smallest = left
            if self._distanceDic.get(self._nodesHeap[index]) <= self._distanceDic.get(self._nodesHeap[smallest]): 
                break
            self._swap(smallest, index)
            index = smallest
            left = 2 * index + 1

    def _heapInsert(self, index):
        parent = int(( index - 1) / 2 )
        while self._distanceDic.get(self._nodesHeap[index]) and self._distanceDic.get(self._nodesHeap[parent]) and \
                self._distanceDic.get(self._nodesHeap[index]) < self._distanceDic.get(self._nodesHeap[parent]):
            self._swap(index, parent)
            #self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = int(( index - 1) / 2 )

    def addOrUpdateOrIgnore(self, node, distance):
        # print("start")
        # print("node:",node.value, node)
        # print("heap", self._nodesHeap)
        if self._inHeap(node): # update
            self._distanceDic[node] =  min(self._distanceDic.get(node), distance)
            self._heapInsert(self._heapIndexDic.get(node))	
        if not self._isEntered(node): # add
            #self._nodesHeap[self._heapsize] = node
            self._nodesHeap.append(node)
            self._heapIndexDic[node] = self._heapsize
            self._distanceDic[node] = distance
            self._heapInsert(self._heapsize)
            self._heapsize+=1
        # print("end")
        # print("node:",node.value, node)
        # print("heap", self._nodesHeap)
        # ignore. do nothing

    def _isEntered(self, node):
        return node in self._heapIndexDic

    def _inHeap(self, node):
        return self._isEntered(node) and self._heapIndexDic.get(node) != -1

    def isEmpty(self):
        return self._heapsize == 0

    def _swap(self, index1, index2):
        self._heapIndexDic[ self._nodesHeap[index1] ] = index2
        self._heapIndexDic[ self._nodesHeap[index2] ] = index1
        self._nodesHeap[index1], self._nodesHeap[index2] = self._nodesHeap[index2], self._nodesHeap[index1]

    def popRecord(self):
        nodeRecord = NodeRecord(self._nodesHeap[0], self._distanceDic.get(self._nodesHeap[0]))
        self._swap(0, self._heapsize-1)
        self._heapIndexDic[self._nodesHeap[self._heapsize-1]] = -1
        del self._distanceDic[self._nodesHeap[self._heapsize-1]]
        self._nodesHeap.pop()
        self._heapsize -= 1
        self._heapify(0)
        return nodeRecord

    def size(self):
        return self._heapsize

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
    lst = dijkstra2(graph.nodes.get(0))
    print( [ (x.node.value, x.distance) for x in lst] )

if __name__ == "__main__":
    main()