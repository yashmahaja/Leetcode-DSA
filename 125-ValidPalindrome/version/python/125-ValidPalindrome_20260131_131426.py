# Last updated: 1/31/2026, 1:14:26 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        
4        res = []
5
6        for i in s:
7            if i.isalnum():
8                res.append(i.lower())
9        
10        ns = "".join(res)
11        i = 0
12        r = len(ns) - 1
13        while i < r:
14            if ns[i] != ns[r]:
15                return False
16            
17            i += 1
18            r -= 1
19        
20        return True