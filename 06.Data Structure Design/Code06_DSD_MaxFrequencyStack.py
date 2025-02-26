############################################################################################
# 最大频率栈
# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
# 实现 FreqStack 类:
# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
# 测试链接 : https://leetcode.cn/problems/maximum-frequency-stack/
############################################################################################

class FreqStack:

    def __init__(self):
        self.maxFreq = 0    # 记录数字出现的最大频次
        self.numsFreq = {}  # 记录每个数字的频次  {num: freq}
        self.freqNums = {}  # 记录不同频次对应的数字  {freq: [num1,num2...]}
        
    def push(self, val: int) -> None:
        self.numsFreq[val] = self.numsFreq.get(val,0) + 1
        freq = self.numsFreq[val] 
        if freq > self.maxFreq :
            self.maxFreq = freq
        if freq in self.freqNums:
            self.freqNums[freq].append(val)
        else:
            self.freqNums[freq] = [val]
        
    def pop(self) -> int:
        if self.maxFreq == 0:
            return None
        res = self.freqNums[self.maxFreq].pop()
        if not self.freqNums[self.maxFreq] or len(self.freqNums[self.maxFreq]) == 0:
            del self.freqNums[self.maxFreq]
            self.maxFreq -= 1
        self.numsFreq[res] -= 1
        if self.numsFreq[res] == 0:
            del self.numsFreq[res]
        return res



#---------------------------------------------------------------------------------

def main():
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4) 
    obj.push(5)
    #print(obj.freqNums,obj.numsFreq,obj.maxFreq)
    print(obj.pop())
    #print(obj.freqNums,obj.numsFreq,obj.maxFreq)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    
if __name__ == "__main__":
    main()