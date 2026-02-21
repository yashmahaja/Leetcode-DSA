# Last updated: 2/21/2026, 10:00:22 AM
1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        
4
5        maps = {}
6        for x in s:
7            maps[x] = 1 + maps.get(x, 0)
8        
9        h = []
10
11        for i, v in maps.items():
12            heapq.heappush(h, [-v, i])
13
14        prev = None
15        res = []
16
17        while h or prev:
18            
19            if not h and prev:
20                return ""
21
22            if h:
23                cnt, char = heapq.heappop(h)
24                res.append(char)
25                cnt += 1
26            
27            if prev:
28                heapq.heappush(h, prev)
29                prev = None
30
31            if cnt < 0:
32                prev = [cnt, char]
33
34
35        return "".join(res)
36            