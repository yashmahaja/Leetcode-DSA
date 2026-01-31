# Last updated: 1/31/2026, 6:21:36 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        
4
5        h = []
6
7        for x, y in points:
8            dis = x*x  + y*y
9            heapq.heappush(h, [-dis, x, y])
10            if len(h) > k:
11                heapq.heappop(h)
12
13        res = []
14        for d, x, y in h:
15                res.append([x, y])
16
17        return res