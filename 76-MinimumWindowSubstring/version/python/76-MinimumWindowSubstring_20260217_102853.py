# Last updated: 2/17/2026, 10:28:53 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        
4        mapt = {}
5        maps = {}
6        l = 0
7        ns = ""
8        minV = float("inf")
9        formed = 0
10
11        for x in t:
12            mapt[x] = 1 + mapt.get(x, 0)
13
14        required = len(mapt)
15
16        for r in range(len(s)):
17            ch = s[r]
18            maps[ch] = 1 + maps.get(ch, 0)
19            
20            if ch in mapt and mapt[ch] == maps[ch]:
21                formed += 1
22            
23            while formed == required:
24                if minV > r - l + 1:
25                    minV = r - l + 1
26                    ns = s[l:r+1]
27                
28                maps[s[l]] -= 1
29
30                if s[l] in mapt and maps[s[l]] < mapt[s[l]]:
31                    formed -= 1
32
33                l += 1
34        
35        return ns