############################################################################################
# 全O(1)的数据结构
# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
# 实现 AllOne 类：
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。
#                   测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
#
# 测试链接 : https://leetcode.cn/problems/all-oone-data-structure/
############################################################################################

class AllOne:

    class Bucket:
        def __init__(self, s, freq):
            self.freq = freq    # 词频  
            self.set = set()    # 在一个桶里存相同词频的所有字符串
            self.set.add(s)
            self.last = None
            self.next = None

    def __init__(self):
        self.head = self.Bucket("", 0) 
        self.tail = self.Bucket("", float("inf"))
        self.head.next = self.tail
        self.tail.last = self.head
        self.dic = {}  # {val: Bucket}

    def insert(self, cur, new):  # 在cur桶后插入new桶
        cur.next.last = new
        new.next = cur.next
        new.last = cur
        cur.next = new
        
    def remove(self, cur):
        cur.last.next = cur.next 
        cur.next.last = cur.last

    def inc(self, key: str) -> None:
        if key not in self.dic: # key不存在
            if self.head.next.freq == 1:  # 有freq为1的Bucket
                self.dic[key] = self.head.next
                self.head.next.set.add(key)
            else: # 没有freq为1的Bucket
                new_bucket = self.Bucket(key, 1)
                self.dic[key] = new_bucket
                self.insert(self.head, new_bucket)
        else: # key存在
            cur = self.dic[key]
            if cur.next.freq == cur.freq + 1:  # cnt+1的桶存在   
                self.dic[key] = cur.next
                cur.next.set.add(key)
            else: #cnt+1的桶不存在
                new_bucket = self.Bucket(key, cur.freq+1)
                self.dic[key] = new_bucket
                self.insert(cur, new_bucket)
            #处理原桶
            cur.set.remove(key)
            if not cur.set:
                self.remove(cur)

    def dec(self, key: str) -> None:
        cur = self.dic[key]
        if cur.freq == 1:
            del self.dic[key]
        else:
            if cur.last.freq + 1 == cur.freq:  #freq少1的桶存在
                self.dic[key] = cur.last
                cur.last.set.add(key)
            else: #freq少1的桶不存在
                new_bucket = self.Bucket(key, cur.freq-1)
                self.dic[key] = new_bucket
                self.insert(cur.last, new_bucket)
        cur.set.remove(key)
        if not cur.set:
            self.remove(cur)

    def getMaxKey(self) -> str:
        if self.tail.last == self.head:
            return ""
        return next(iter(self.tail.last.set))
        
    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.set))





#---------------------------------------------------------------------------------

def main():
    obj = AllOne()
    obj.inc("hello")
    obj.dec("hello")
    print(obj.getMaxKey())
    print(obj.getMinKey())
    obj.inc("leet")
    print(obj.getMaxKey())
    print(obj.getMinKey())

    
if __name__ == "__main__":
    main()