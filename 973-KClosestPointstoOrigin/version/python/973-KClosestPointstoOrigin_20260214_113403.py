# Last updated: 2/14/2026, 11:34:03 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        
4
5        h = []
6
7        for x, y in points:
8            d = x * x + y * y
9            heapq.heappush(h, [-d,x,y])
10            if len(h) > k:
11                heapq.heappop(h)
12            
13
14        ans = []
15
16        for d, x, y in h:
17            ans.append([x,y])
18        
19        return ans