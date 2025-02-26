############################################################################################
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

# 测试链接 : https://leetcode.cn/problems/find-median-from-data-stream/
############################################################################################

import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxHeap or num < self.maxHeap[0][1]:
            heapq.heappush(self.maxHeap, [-num, num])
        else:
            heapq.heappush(self.minHeap, [num, num])

        # balance
        if len(self.minHeap) - len(self.maxHeap) == 2:
            _, num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, [-num, num])
        elif len(self.maxHeap) - len(self.minHeap) == 2:
            _, num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, [num, num])

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            return None
        elif (len(self.minHeap) == len(self.maxHeap)) :
            return (self.minHeap[0][1] + self.maxHeap[0][1]) * 1.0 / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0][1]
        else:
            return self.maxHeap[0][1]


#---------------------------------------------------------------------------------

def main():
    obj = MedianFinder()
    print(obj.findMedian())
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)       

    print(obj.maxHeap, obj.minHeap)

    print(obj.findMedian())
    
if __name__ == "__main__":
    main()