# Last updated: 2/2/2026, 9:58:20 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        
4
5        col = set()
6        pd = set()
7        nd = set()
8        b = [["."] * n for _ in range(n)]
9        ans = []
10
11        def back(r):
12            if r >=n:
13                ans.append(["".join(x) for x in b])
14                return
15
16            for c in range(n):
17                if c  in col or  r + c in pd or r - c in nd:
18                    continue
19
20                col.add(c)
21                pd.add(r+c)
22                nd.add(r-c)
23                b[r][c] = "Q"
24
25                back(r+1)
26
27                col.remove(c)    
28                pd.remove(r+c)
29                nd.remove(r-c)
30                b[r][c] = "."
31        
32        back(0)
33        return ans