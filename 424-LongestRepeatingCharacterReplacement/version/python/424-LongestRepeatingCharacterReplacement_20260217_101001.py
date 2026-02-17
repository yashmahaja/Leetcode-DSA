# Last updated: 2/17/2026, 10:10:01 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        
4
5        l = 0 
6        maxi = 0
7        maps = {}
8        for r in range(len(s)):
9            maps[s[r]] = 1 + maps.get(s[r], 0)
10
11            if (r - l + 1 ) - max(maps.values()) > k:
12                maps[s[l]] -= 1
13                if maps[s[l]] == 0:
14                    del maps[s[l]]
15                l += 1
16            
17            maxi = max(maxi, r - l + 1)
18        
19        return maxi