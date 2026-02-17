# Last updated: 2/17/2026, 10:30:46 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        
4
5        mapt = {}
6        maps = {}
7        l = 0 
8        minV = float("inf")
9        res = ""
10
11        formed = 0
12        
13
14        for x in t:
15            maps[x] = 1 + maps.get(x, 0)
16
17        required = len(maps)
18
19        for r in range(len(s)):
20            ch = s[r]
21            mapt[ch] = 1 + mapt.get(ch, 0)
22
23            if ch in maps and maps[ch] == mapt[ch]:
24                formed += 1
25
26            while formed == required:
27                if r - l + 1 < minV:
28                    minV = r - l + 1
29                    res = s[l : r + 1]
30                
31                mapt[s[l]] -= 1
32                if s[l] in maps and mapt[s[l]] < maps[s[l]]:
33                    formed -= 1
34                
35                l += 1
36        
37        return res
38
39
40