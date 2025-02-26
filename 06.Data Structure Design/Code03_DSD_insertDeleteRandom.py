############################################################################################
# 实现RandomizedSet 类：

# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

# https://leetcode.cn/problems/insert-delete-getrandom-o1
############################################################################################

import random

class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.lst)
        self.lst.append(val)
        return True
         
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        val_idx = self.dic[val]
        end_val = self.lst[-1]
        
        self.dic[end_val] = val_idx
        self.dic.pop(val)
        
        self.lst[val_idx] = end_val
        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)

    
#---------------------------------------------------------------------------------

def main():
    obj = RandomizedSet()
    # print(obj.insert(1))
    # print(obj.remove(2))
    # print(obj.insert(2))
    # print(obj.getRandom())
    # print(obj.remove(1))
    # print(obj.insert(2))
    # print(obj.getRandom())


    print(obj.remove(0))
    print(obj.remove(0))
    print(obj.insert(0))
    print(obj.getRandom())
    print(obj.dic, obj.lst)
    print(obj.remove(0))
    print(obj.dic, obj.lst)
    print(obj.insert(0))



if __name__ == "__main__":
    main()