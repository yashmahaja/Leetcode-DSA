# Last updated: 2/16/2026, 9:35:02 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        
4        dp = [-1] * len(s)
5
6        def rec(i):
7            if i >= len(s):
8                return 1
9
10            if dp[i] != -1:
11                return dp[i]
12
13            if s[i] == '0':
14                return 0
15
16            ways = rec(i+1)
17
18            if i + 2 <= len(s) and 10 <= int(s[i:i+2]) <= 26:
19                ways += rec(i+2)
20
21            dp[i] = ways
22            return dp[i]
23
24        return rec(0)