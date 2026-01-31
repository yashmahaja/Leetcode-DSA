# Last updated: 1/31/2026, 6:11:33 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        
4        stones =  [-s for s in stones]
5        heapq.heapify(stones)
6
7        while len(stones) > 1:
8            f = heapq.heappop(stones)
9            s = heapq.heappop(stones)
10
11            if f != s:
12                heapq.heappush(stones, f - s)
13        
14        heapq.heappush(stones, 0)
15        return -stones[0]