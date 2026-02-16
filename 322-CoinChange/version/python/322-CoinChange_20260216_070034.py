# Last updated: 2/16/2026, 7:00:34 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        
4        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
5        def rec(i,x):
6            if x == 0:
7                return 0
8
9            if i >= len(coins) or x < 0:
10                return float("inf")
11
12            if dp[i][x] != -1:
13                return dp[i][x]
14
15            take = 0
16            if x > 0:
17                take = 1 + rec(i,x - coins[i])
18
19            nott = rec(i+1,x)
20            dp[i][x] =  min(take, nott)
21            return dp[i][x]
22
23        ans = rec(0, amount)
24        if ans == float('inf'):
25            return -1
26        return ans