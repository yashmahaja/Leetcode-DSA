# Last updated: 2/20/2026, 5:10:27 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        
4        maps  = {}
5
6        for x in tasks:
7            maps[x] = 1 + maps.get(x, 0)
8        
9        h = []
10
11        for ch,val in maps.items():
12            h.append(-val)
13        
14        heapq.heapify(h)
15        time = 0
16
17        some = deque()
18
19        while h or some:
20            time += 1
21
22            if h:
23                val = heapq.heappop(h)
24                val += 1
25                if val < 0:
26                    some.append((val, time + n))
27            
28            if some and some[0][1] == time:
29                value, time = some.popleft()
30                heapq.heappush(h,value)
31        
32        return time