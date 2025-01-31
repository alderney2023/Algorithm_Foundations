###########################################################################
#   并查集 灵活字典版
###########################################################################

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

def main():
    lst = [10,20,30,40,50,60,70,80]
    us = UnionSet(lst)
    # print(us.nodes)
    # print(us.sizeMap)
    us.union(10,30)
    us.union(10,20)
    print(us.findFather(10))
    print(us.sizeMap)
    print(us.isSameSet(20,30))


if __name__ == "__main__":
    main()