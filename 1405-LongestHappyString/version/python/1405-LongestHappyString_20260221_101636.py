# Last updated: 2/21/2026, 10:16:36 AM
1class Solution:
2    def longestDiverseString(self, a: int, b: int, c: int) -> str:
3        
4        maps = {'a': -a, 'b' : -b, 'c' : -c}
5
6        h = []
7
8        for char, cnt in maps.items():
9            if cnt < 0:
10                heapq.heappush(h, [cnt, char])
11        
12        res = []
13        while h:
14
15            cnt, char = heapq.heappop(h)
16
17            if  len(res) >= 2 and res[-1] == res[-2] == char:
18
19                if not h:
20                    break
21
22                cnt2, char2 = heapq.heappop(h)
23                cnt2 += 1
24
25                if cnt2 < 0:
26                    heapq.heappush(h, [cnt2, char2])
27
28                res.append(char2)
29                heapq.heappush(h, [cnt, char])
30
31            else:
32                cnt += 1
33                res.append(char)
34                if cnt < 0:
35                    heapq.heappush(h,[cnt,char])
36        
37        return "".join(res)
38