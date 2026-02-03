# Last updated: 2/2/2026, 9:03:47 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        
4        ans = []
5        def isPal(i,j):
6            if i >= j:
7                return True
8
9            if s[i] != s[j]:
10                return False
11            
12            elif s[i] == s[j]:
13                return isPal(i+1, j-1)
14
15        def back(i, temp):
16            if i >= len(s):
17                ans.append(temp[:])
18                return
19                
20            for x in range(i, len(s)):
21                    if isPal(i,x):
22                        temp.append(s[i:x+1])
23                        back(x+1, temp)
24                        temp.pop()
25
26        back(0, [])
27        return ans