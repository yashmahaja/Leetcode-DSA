# Last updated: 2/16/2026, 6:16:56 AM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        
4        dp = [-1] * len(cost)
5        def solve(i):
6            if i >= len(cost):
7                return 0
8            
9            if dp[i] != -1:
10                return dp[i]
11            
12            l = cost[i] + solve(i + 1)
13            r = cost[i] + solve(i + 2)
14
15            dp[i] =  min(l,r)
16            return dp[i]
17
18        return min(solve(0),solve(1))
19        