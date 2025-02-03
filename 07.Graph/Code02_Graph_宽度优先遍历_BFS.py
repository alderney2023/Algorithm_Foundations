###########################################################################
#   宽度优先遍历 BFS
#       借用一个queue, 一个set，  出stack打印
###########################################################################

from Code01_Graph_Defination import Node, Edge, Graph, createGraph


def BFS(start):
    if not start:
        return 
    queue = [start]
    s = set()         #  ***
    s.add(start)  
    while queue:
        cur = queue.pop(0)
        print(cur.value, end=" ")
        for next in cur.nexts:
            if next not in s:  #  ***
                queue.append(next)
                s.add(next)  #  ***
    print()

 #---------------------------------------------------------------------------------


def main():
    g = [ [ 5 , 0 , 2],
          [ 3 , 0,  1],
          [ 10, 1,  4],
          [ 8,  2,  3] ]
    graph = createGraph(g)
    BFS(graph.nodes.get(0))
    

if __name__ == "__main__":
    main()