# Last updated: 2/1/2026, 10:23:43 AM
1class Solution:
2    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
3        
4
5        cp = sorted(zip(capital,profits))
6        h = []
7        i = 0
8        while h or i < len(cp):
9
10            while i < len(cp) and cp[i][0] <= w:
11                cap, profit = cp[i]
12                heapq.heappush(h, -profit)
13                i += 1
14            
15            if not h: 
16                break
17
18            pro = heapq.heappop(h)
19            w += -pro
20            k -= 1
21
22            if k == 0:
23                return w
24        
25        return w