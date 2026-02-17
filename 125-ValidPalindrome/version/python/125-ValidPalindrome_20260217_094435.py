# Last updated: 2/17/2026, 9:44:35 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        
4        res = []
5        for x in s:
6            if x.isalnum():
7                res.append(x.lower())
8
9        ns =  "".join(res)
10
11        l = 0
12        r = len(ns) - 1
13
14        while l < r:
15            if ns[l] != ns[r]:
16                return False
17            
18            l += 1
19            r -= 1
20        
21        return True
22