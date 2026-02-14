# Last updated: 2/14/2026, 11:23:28 AM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        
4        stones = [-s for s in stones]
5        heapq.heapify(stones)
6
7        while len(stones) > 1:
8
9            big = heapq.heappop(stones)
10            small = heapq.heappop(stones)
11
12            if small != big:
13                heapq.heappush(stones, (big - small))
14            
15
16        heapq.heappush(stones, 0)
17        return -stones[0]