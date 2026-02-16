# Last updated: 2/16/2026, 4:11:53 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        
4        row = {i:set() for i in range(9)}
5        col = {i:set() for i in range(9)}
6        b = {(i,j): set() for i in range(3) for j in range(3)}
7
8        for i in range(9):
9            for j in range(9):
10                val = board[i][j]
11                if val == ".":
12                    continue
13                
14                if val in row[i] or val in col[j] or val in b[(i//3,j//3)]:
15                    return False
16                
17
18                row[i].add(val)
19                col[j].add(val)
20                b[(i//3, j // 3)].add(val)
21        
22        return True
23
24