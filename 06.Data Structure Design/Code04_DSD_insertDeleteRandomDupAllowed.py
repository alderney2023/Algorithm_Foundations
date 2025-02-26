############################################################################################
# RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。
# 实现 RandomizedCollection 类:
# RandomizedCollection()初始化空的 RandomizedCollection 对象。
# bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
# bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
# int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
# 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。
#
# 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。
#
#https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/
############################################################################################

import random

class RandomizedCollection:

    def __init__(self):
        self.dic = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:
        self.lst.append(val)
        n =len(self.lst)
        if val in self.dic:
            self.dic[val].add(n-1)
            return False
        else:
            s = set()
            s.add(n-1)
            self.dic[val] = s
            return True
         
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        val_set = self.dic[val]
        val_any_idx = next(iter(val_set))
        val_end = self.lst[-1]
        if val == val_end:
            val_set.remove(len(self.lst)-1)
        else:
            end_val_set = self.dic[val_end]
            end_val_set.add(val_any_idx)
            self.lst[val_any_idx] = val_end
            end_val_set.remove(len(self.lst)-1)
            val_set.remove(val_any_idx)

        self.lst.pop()
        if not val_set:
            del self.dic[val]
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
    
#---------------------------------------------------------------------------------

def main():
    obj = RandomizedCollection()

    print(obj.insert(1))
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.getRandom())
    print(obj.dic, obj.lst)



if __name__ == "__main__":
    main()