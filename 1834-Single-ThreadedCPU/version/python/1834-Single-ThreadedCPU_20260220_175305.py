# Last updated: 2/20/2026, 5:53:05 PM
1class Solution:
2    def getOrder(self, tasks: List[List[int]]) -> List[int]:
3        
4        h = []
5
6        s = sorted([[en, pt, idx] for idx, (en, pt) in enumerate(tasks)])
7
8        i = 0
9        ans = [] 
10        time = 0
11        while i < len(s) or h:
12
13            if not h and time <= s[i][0]:
14                time = s[i][0]
15
16            while i < len(s) and s[i][0] <= time:
17                et,pt,idx = s[i]
18                heapq.heappush(h,[pt,idx])
19                i += 1
20            
21            if h:
22                pt, idx = heapq.heappop(h)
23
24            time += pt
25            ans.append(idx)
26        
27        return ans