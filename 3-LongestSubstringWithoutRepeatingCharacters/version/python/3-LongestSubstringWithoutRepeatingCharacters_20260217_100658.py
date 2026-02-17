# Last updated: 2/17/2026, 10:06:58 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        
4        cs = set()
5        l = 0
6        maxi = 0
7        for r in range(len(s)):
8            while s[r] in cs:
9                cs.remove(s[l])
10                l += 1
11            
12            cs.add(s[r])
13            maxi = max(maxi, r - l + 1)
14        
15        return maxi