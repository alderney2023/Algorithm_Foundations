
###########################################################################
#   并查集 范围数字 数组版
#   优点： 速度快
#   缺点： 整体集合限制为 0 - maxval 的所有数字 
###########################################################################

class UnionSet:

    def __init__(self, maxval):
        self.father = [ i for i in range(maxval+1) ]   
        self.size = [1] * (maxval+1)  #只有每个set的头节点值才非0

    def findFather(self, v):
        if v not in self.father : 
            return
        stack = []
        while self.father[v] != v:
            stack.append()
            v = self.father[v]
        while stack:
            self.father[stack.pop()] = v
        return v

    def isSameSet(self, v1, v2):
        return self.findFather(v1) == self.findFather(v2)

    def union(self, v1, v2):
        if self.isSameSet(v1, v2):
            return 
        a = self.findFather(v1)
        b = self.findFather(v2)
        if self.size[a] >= self.size[b]:
            large, small = a, b
        else:
            large, small = b, a
        self.father[small] = large
        self.size[large] += self.size[small]
        self.size[small] = 0

    def sizeSets(self):
        return len( [x for x in self.size if x!=0 ] )


#---------------------------------------------------------------------------------

def main():
    us = UnionSet(80)

    print(us.findFather(10))
    print(us.findFather(30))
    print(us.isSameSet(10,30))

    # print(us.nodes)
    # print(us.size)
    us.union(10,30)
    us.union(10,20)

    print(us.isSameSet(20,30))


if __name__ == "__main__":
    main()