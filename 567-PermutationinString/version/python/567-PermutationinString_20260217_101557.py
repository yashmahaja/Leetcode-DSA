# Last updated: 2/17/2026, 10:15:57 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        
4        if len(s1) > len(s2):
5            return False
6        
7        need = [0] * 26
8        win = [0] * 26
9
10        for x in s1:
11            need[ord(x) - ord('a')] += 1
12        
13        for x in range(len(s2)):
14            ch = s2[x]
15
16            win[ord(ch) - ord('a')] += 1
17
18            if x >= len(s1):
19                win[ord(s2[x - len(s1)]) - ord('a')] -= 1
20            
21            if need == win:
22                return True
23        
24        return False