# Last updated: 2/14/2026, 12:17:08 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        
4
5        maps = {}
6
7        for x in tasks:
8            maps[x] = 1 + maps.get(x, 0)
9        
10        h = []
11        for x, y in maps.items():
12            heapq.heappush(h, [-y, x])
13
14        time = 0
15        q = deque()
16
17        while h or q:
18            time += 1
19
20            if h:
21                cnt, val = heapq.heappop(h)
22                cnt += 1
23                if cnt < 0:
24                    q.append((cnt, val, time + n))
25            
26            if q and q[0][2] == time:
27                c, val, t = q.popleft()
28                heapq.heappush(h,[c,val])
29
30        return time