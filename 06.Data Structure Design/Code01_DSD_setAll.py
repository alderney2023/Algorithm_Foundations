############################################################################################
# setAll功能的哈希表
# 哈希表常见的三个操作时put、get和containsKey，而且这三个操作的时间复杂度为O(1)。
# 现在想加一个setAll功能，就是把所有记录value都设成统一的值。请设计并实现这种有setAll功能的哈希表，
# 并且put、get、containsKey和setAll四个操作的时间复杂度都为O(1)。
#
# 测试链接 : https://www.nowcoder.com/practice/7c4559f138e74ceb9ba57d76fd169967
############################################################################################


class SetAllHashMap:
    def __init__(self):
        self.dic = {}
        self.setAllValue = 0
        self.setAllTime = 0
        self.cnt = 0

    def setAll(self, val):
        self.setAllValue = val
        self.cnt += 1
        self.setAllTime = self.cnt
        
    def put(self, key, val):
        if key in self.dic:
            value = self.dic[key]
            value[0] = val
            self.cnt += 1 
            value[1] = self.cnt
        else:
            value = [0] * 2
            self.dic[key] = value
            value[0] = val
            self.cnt += 1
            value[1] = self.cnt    
    
    def get(self, key):
        if key not in self.dic:
            return -1
        else:
            if self.dic[key][1] > self.setAllTime:
                return self.dic[key][0]
            else:
                return self.setAllValue


def main():
    sa = SetAllHashMap()
    sa.put(1,1)
    sa.put(2,2)
    sa.setAll(3)
    print(sa.get(1))
    sa.put(2,4)
    print(sa.get(2))

if __name__ == "__main__":
    main()
