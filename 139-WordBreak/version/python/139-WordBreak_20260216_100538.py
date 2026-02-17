# Last updated: 2/16/2026, 10:05:38 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        
4        wD = set(wordDict)
5        dp = [None] * len(s)
6        
7        def cbreak(i):
8            if i >= len(s):
9                return True
10            
11            if dp[i] != None:
12                return dp[i]
13
14            for j in range(i, len(s)):
15                if s[i:j+1] in wD:
16                    if cbreak(j+1):
17                        dp[i] = True
18                        return True
19
20            dp[i] =  False
21            return dp[i]    
22    
23        return cbreak(0)