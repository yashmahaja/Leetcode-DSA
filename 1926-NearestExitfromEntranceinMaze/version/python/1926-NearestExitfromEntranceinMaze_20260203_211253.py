# Last updated: 2/3/2026, 9:12:53 PM
1class Solution:
2    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
3        
4        m = len(maze)
5        n = len(maze[0])
6        er, ec = entrance
7        q = deque([(entrance[0], entrance[1], 0)])
8        visit = set()
9        visit.add((entrance[0], entrance[1]))
10
11        directions = [[1,0], [0,1], [-1,0], [0,-1]]
12        
13        while q:
14            r, c, steps = q.popleft()
15
16            if (r in [m-1, 0] or c in [n-1,0]) and (r,c) != (er,ec): 
17                return steps
18
19            for row, col in directions:
20                nr = row + r
21                nc = col + c
22
23                if nr < 0 or nc < 0 or nr >= m or nc >= n or (nr,nc) in visit:
24                    continue
25                
26                if maze[nr][nc] == "+":
27                    continue
28                
29                q.append((nr, nc, steps + 1))
30                visit.add((nr,nc))
31        
32        return -1