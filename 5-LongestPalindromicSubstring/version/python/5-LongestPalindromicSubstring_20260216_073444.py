# Last updated: 2/16/2026, 7:34:44 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        
4        dp = [[None] * len(s) for _ in range(len(s))]
5
6        def solve(i, j):
7
8            if i >= j:
9                return True
10
11            if dp[i][j] is not None:
12                return dp[i][j]
13
14            if s[i] != s[j]:
15                dp[i][j] =  False
16            else:
17                dp[i][j] = solve(i + 1, j - 1)
18
19            return dp[i][j]
20
21        sp = 0
22        maxi = 0
23        for i in range(len(s)):
24            for j in range(i, len(s)):
25                if solve(i, j):
26                    if j - i + 1 > maxi:
27                        maxi = j - i + 1
28                        sp = i
29        
30        return s[sp:sp + maxi]
31