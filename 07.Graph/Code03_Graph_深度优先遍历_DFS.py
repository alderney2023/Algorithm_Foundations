###########################################################################
#   深度优先遍历 DFS
#       借用一个stack, 一个set, 进set打印
###########################################################################

from Code01_Graph_Defination import Node, Edge, Graph, createGraph

def DFS(start):
    if not start:
        return
    stack = [start]
    s = set()
    s.add(start) 
    print(start.value, end=" ")
    while stack:
        cur = stack.pop()
        for next in cur.nexts:
            if next not in s:
                stack.append(cur)
                stack.append(next)
                s.add(next)
                print(next.value, end=" ")
                break
    print()


#---------------------------------------------------------------------------------

def main():
    g = [ [ 5 , 0 , 2],
          [ 3 , 0,  1],
          [ 10, 1,  4],
          [ 8,  2,  3] ]
    graph = createGraph(g)
    DFS(graph.nodes.get(0))
    

if __name__ == "__main__":
    main()