# Last updated: 2/17/2026, 10:16:25 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        
4        if len(s1) > len(s2):
5            return False
6
7        maps = {}
8        mapt = {}
9        l = 0
10
11        for x in s1:
12            maps[x] = 1 + maps.get(x, 0)
13
14        for r in range(len(s2)):
15            ch = s2[r]
16            mapt[ch] = 1 + mapt.get(ch, 0)
17
18            while r - l + 1 > len(s1):
19                mapt[s2[l]] -= 1
20                if mapt[s2[l]] == 0:
21                    del mapt[s2[l]]
22                l += 1
23            
24            if mapt == maps:
25                return True
26        
27        return False