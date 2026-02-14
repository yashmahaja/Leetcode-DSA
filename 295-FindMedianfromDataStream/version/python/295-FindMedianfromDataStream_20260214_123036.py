# Last updated: 2/14/2026, 12:30:36 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.hmin = []
5        self.hmax = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.hmax, -num)
9        heapq.heappush(self.hmin, -heapq.heappop(self.hmax))
10        if len(self.hmax) < len(self.hmin):
11            heapq.heappush(self.hmax, -heapq.heappop(self.hmin))
12
13    def findMedian(self) -> float:
14        if len(self.hmin) == len(self.hmax):
15            return (self.hmin[0] + (-self.hmax[0])) / 2.0
16        else:
17            return float(-self.hmax[0])
18# Your MedianFinder object will be instantiated and called as such:
19# obj = MedianFinder()
20# obj.addNum(num)
21# param_2 = obj.findMedian()