# Last updated: 2/20/2026, 5:27:52 PM
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
13
14    def findMedian(self) -> float:
15        if (len(self.hmin) + len(self.hmax)) % 2 != 0:
16            return -self.hmax[0]
17        else:
18            return (-self.hmax[0] + self.hmin[0]) / 2.0
19
20
21# Your MedianFinder object will be instantiated and called as such:
22# obj = MedianFinder()
23# obj.addNum(num)
24# param_2 = obj.findMedian()