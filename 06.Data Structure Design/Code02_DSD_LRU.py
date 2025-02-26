###########################################################################
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
#                              如果不存在，则向缓存中插入该组 key-value 。
#                              如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
# 测试链接 : https:#leetcode.cn/problems/lru-cache/
###########################################################################

class DoubleNode:
    def __init__(self,key, val, next=None,last=None):
        self.key = key
        self.val = val
        self.next = next
        self.last = last

class DoubleList:
    def __init__(self,head = None, tail = None):    
        self.head = head
        self.tail = tail

    def addNode(self,node):
        if not node:
            return 
        if not self.head:
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node 
            node.last = self.tail
            self.tail = node 

    def removeHead(self):
        if not self.head:
            return None
        ans = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            print("hear", self.head.val, self.tail.val)
            self.head = self.head.next
            self.head.last = None
            ans.next = None
            print("hear", self.head.val, self.tail.val)
        return ans.key

    def moveNodeToTail(self, node):
        if not node:
            return 
        if node == self.tail:
            return 
        if self.head == node:
            self.head = self.head.next
            self.head.last = None
        else:
            print(node.val)
            print( self.head.val, self.tail.val)
            node.last.next = node.next
            node.next.last = node.last
        self.tail.next = node
        node.last = self.tail
        node.next = None
        self.tail = node

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}      # {  key:DoubleNode}
        self.doubleList = DoubleList()    
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.doubleList.moveNodeToTail(self.dic[key])
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.doubleList.moveNodeToTail(self.dic[key])
        else:
            print("dic size:",len(self.dic))
            if len(self.dic) == self.capacity:
                del_key = self.doubleList.removeHead()
                del self.dic[del_key]
            print("dic size:",len(self.dic))   
            node = DoubleNode(key, value)
            self.dic[key] = node
            self.doubleList.addNode(node)


#---------------------------------------------------------------------------------

def main():
    capacity = 2
    obj = LRUCache(capacity)
    
    obj.put(1, 1) # 缓存是 {1=1}
    obj.put(2, 2) # 缓存是 {1=1, 2=2}
    print(obj.get(1))    # 返回 1
    obj.put(3, 3) # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(obj.get(2))    # 返回 -1 (未找到)
    obj.put(4, 4) # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(obj.get(1))    # 返回 -1 (未找到)
    print(obj.get(3))    # 返回 3
    print(obj.get(4))    # 返回 4


if __name__ == "__main__":
    main()


