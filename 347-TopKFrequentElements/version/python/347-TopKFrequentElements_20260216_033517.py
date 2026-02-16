# Last updated: 2/16/2026, 3:35:17 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        
4        h = []
5        maps = {}
6        for x in nums:
7            maps[x] = 1 + maps.get(x,0)
8        
9        for value, cnt in maps.items():
10            heapq.heappush(h,[cnt,value])
11            if len(h) > k:
12                heapq.heappop(h)
13            
14        res = []
15        for count, val in h:
16            res.append(val)
17
18        return res
19