# Last updated: 2/16/2026, 3:30:19 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        maps = {}
5        for word in strs:
6            count = [0] * 26
7            for x in word:
8                count[ord(x) - ord('a')] += 1
9
10
11            count = tuple(count)
12            if count not in maps:
13                maps[count] = []
14
15            maps[count].append(word)
16        
17        return list(maps.values())