# Last updated: 2/16/2026, 6:31:43 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3    
4        dp = [-1] * (n + 1)
5        def solve(i):
6            if i > n:
7                return 0
8            
9            if dp[i] != -1:
10                return dp[i]
11
12            if i == n:
13                return 1
14            
15            l = solve(i + 1)
16            r = solve(i + 2)
17            
18            dp[i] = l + r
19            return dp[i]
20
21        return solve(0)