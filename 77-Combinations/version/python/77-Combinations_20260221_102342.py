# Last updated: 2/21/2026, 10:23:42 AM
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        
4        ans = []
5        def rec(i, temp):
6            if len(temp) == k:
7                ans.append(temp[:])
8                return
9            
10            for x in range(i, n + 1):
11                temp.append(x)
12                rec(x + 1, temp)
13                temp.pop()
14        
15
16        rec(1, [])
17        return ans