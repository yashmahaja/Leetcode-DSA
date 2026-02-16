# Last updated: 2/16/2026, 7:03:53 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        
4        dp = [[-1] * (amount + 1) for i in range(len(coins))]
5        def solve(i,add):
6            if add == amount:
7                return 0
8
9            if i >= len(coins):
10                return float("inf")
11            
12            
13            if dp[i][add] != -1:
14                return dp[i][add]
15
16            if add > amount:
17                return float("inf") 
18            
19            l = float("inf")
20            if coins[i] + add <= amount:
21                l = 1 + solve(i,add + coins[i])
22
23            r = solve(i + 1,add)
24
25            dp[i][add] =  min(l,r)
26            return dp[i][add]
27
28        return solve(0,0) if solve(0,0) != float("inf") else -1