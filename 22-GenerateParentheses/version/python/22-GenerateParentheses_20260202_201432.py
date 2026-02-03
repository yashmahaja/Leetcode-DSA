# Last updated: 2/2/2026, 8:14:32 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        
4        ans = []
5        def rec(o, c, temp):
6            if len(temp) == 2 * n:
7                ans.append("".join(temp))
8                return
9
10            if o < n:
11                temp.append("(")
12                rec(o+1, c, temp)
13                temp.pop()
14            
15            if c < o:
16                temp.append(")")
17                rec(o, c + 1, temp)
18                temp.pop()
19        
20        rec(0,0, [])
21        return ans 
22