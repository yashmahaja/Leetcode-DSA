# Last updated: 2/14/2026, 4:30:49 PM
1class Trie:
2    def __init__(self):
3        self.child = {}
4        self.w = False
5    
6    def addWords(self,word):
7        root = self
8        for c in word:
9            if c not in root.child:
10                root.child[c] = Trie()
11            root = root.child[c]
12        root.w = True
13
14
15class Solution:
16    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
17        root = Trie()
18        for x in words:
19            root.addWords(x)
20        
21        res = set()
22        visit = set()
23        def dfs(r,c,curr,word):
24            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visit:
25                return
26            
27            if board[r][c] not in curr.child:
28                return
29            
30            visit.add((r,c))
31            curr = curr.child[board[r][c]]
32            word += board[r][c]
33            if curr.w:
34                res.add(word)
35            
36            dfs(r - 1, c, curr, word)
37            dfs(r + 1, c, curr, word)
38            dfs(r, c - 1, curr, word)
39            dfs(r, c + 1, curr, word)
40            visit.remove((r,c))
41
42    
43
44        for x in range(len(board)):
45            for y in range(len(board[0])):
46                dfs(x,y,root,"")
47
48        return list(res)