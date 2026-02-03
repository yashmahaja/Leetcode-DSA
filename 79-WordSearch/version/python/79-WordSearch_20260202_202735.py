# Last updated: 2/2/2026, 8:27:35 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        
4        m = len(board)
5        n = len(board[0])
6
7
8        def dfs(row, col, idx):
9            
10            if len(word) == idx:
11                return True
12
13            if row < 0 or col < 0 or row >= m or col >= n or word[idx] != board[row][col]:
14                return False
15            
16            temp = board[row][col]
17            board[row][col] = "#"
18
19            res = (dfs(row + 1, col, idx+1) or 
20            dfs(row, col + 1, idx+1) or
21            dfs(row-1, col, idx+1) or
22            dfs(row, col - 1, idx+1))
23            
24            board[row][col] = temp
25
26            return res
27
28        for r in range(m):
29            for c in range(n):
30                if dfs(r, c, 0):
31                    return True
32        
33
34        return False