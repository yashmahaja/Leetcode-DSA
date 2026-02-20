# Last updated: 2/20/2026, 4:35:44 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        
4        s = [-s for s in stones]
5
6        heapq.heapify(s)
7
8        while len(s) > 1:
9
10            first = heapq.heappop(s)
11            sec = heapq.heappop(s)
12
13            if sec != first:
14                heapq.heappush(s, first - sec)
15        
16        heapq.heappush(s,0)
17        return -s[0]