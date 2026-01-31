# Last updated: 1/31/2026, 1:24:12 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        
4
5        res = []
6
7        l = 0
8        r = 0
9
10        while l < len(word1) and r < len(word2):
11            res.append(word1[l])
12            res.append(word2[r])
13
14            l += 1
15            r += 1
16        
17        res.extend(word1[l:])
18        res.extend(word2[r:])
19
20        return "".join(res)
21
22        