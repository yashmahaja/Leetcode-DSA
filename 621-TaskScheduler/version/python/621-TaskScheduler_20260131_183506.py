# Last updated: 1/31/2026, 6:35:06 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3
4        maps = {}
5        for x  in tasks:
6            maps[x] = 1 + maps.get(x, 0)
7
8        time = 0
9        q = deque()
10        h = []
11
12        for i, v in maps.items():
13            heapq.heappush(h, [-v, i])
14
15        while h or q:
16            time += 1
17
18            if h:
19                count, al = heapq.heappop(h) 
20                count += 1
21                if count < 0:
22                    q.append((count, al, time + n))
23
24                
25            if q and q[0][2] == time:
26                cnt, al, ti = q.popleft()
27                heapq.heappush(h, [cnt, al])
28        
29        return time