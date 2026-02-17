# Last updated: 2/17/2026, 11:15:09 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        
4        maps =  {")":"(", "}":"{", "]":"["}
5        res = []
6
7        for x in s:
8            if x in maps.values():
9                res.append(x)
10            
11            else:
12                if not res or res.pop() != maps[x]:
13                    return False
14        
15        return not res