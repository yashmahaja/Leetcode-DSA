# Last updated: 2/16/2026, 10:04:35 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        word_set = set(wordDict)
4        n  = len(s)
5        dp = [None] * n
6
7        def can_break(i):
8            if i == n:
9                return True
10            
11            if  dp[i] != None:
12                return dp[i]
13
14            for j in range(i + 1, n + 1):
15                if s[i:j] in word_set:
16                    if can_break(j):
17                        dp[i] =  True
18                        return True
19            
20            dp[i] =  False
21            return dp[i]
22
23        return can_break(0)