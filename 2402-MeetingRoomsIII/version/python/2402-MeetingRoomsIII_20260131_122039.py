# Last updated: 1/31/2026, 12:20:39 PM
1class Solution:
2    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
3        
4
5        sm = sorted([(s, e, i ) for i, (s, e) in enumerate(meetings)])
6 
7        roomc = [0] * n
8        avail = list(range(n))
9        heapq.heapify(avail)
10        h = []
11
12        for s, e, idx in sm:
13
14            while h and h[0][0] <= s:
15                end, room = heapq.heappop(h)
16                heapq.heappush(avail, room)
17            
18            if avail:
19                room = heapq.heappop(avail)
20                heapq.heappush(h, (e,room))
21                roomc[room] += 1
22            
23            else:
24                mine, i = heapq.heappop(h)
25                heapq.heappush(h, (mine + (e-s), i))
26                roomc[i] += 1
27        
28        best = 0
29        for x in range(1, n):
30            if roomc[x] > roomc[best]:
31                best = x
32        
33        return best