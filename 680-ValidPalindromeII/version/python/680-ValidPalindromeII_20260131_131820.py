# Last updated: 1/31/2026, 1:18:20 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        
4        l = 0
5        r = len(s) - 1
6
7        def pallindrome(p, q):
8            while p  < q:
9                if s[p] != s[q]:
10                    return False
11                
12                p += 1
13                q -= 1
14            
15            return True
16        
17        while l < r:
18            if s[l] != s[r]:
19                return pallindrome(l,r - 1) or pallindrome(l + 1, r)
20
21            l += 1
22            r -= 1
23
24        return True 