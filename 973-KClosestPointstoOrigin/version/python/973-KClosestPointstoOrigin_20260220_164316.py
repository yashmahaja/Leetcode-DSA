# Last updated: 2/20/2026, 4:43:16 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        
4        h = []
5        for x, y in points:
6            d = x * x + y * y 
7            heapq.heappush(h, [d,x,y])
8
9        heapq.heapify(h)
10
11        ans = []
12        for x in range(k):
13            _, i ,j = heapq.heappop(h)
14            ans.append([i,j])
15        
16        return ans