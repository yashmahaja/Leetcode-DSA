# Last updated: 2/15/2026, 11:21:30 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        
4
5        i = 0
6        ans = []
7        ns, ne = newInterval
8        while i < len(intervals):
9            cs, ce = intervals[i]
10
11            if ns <= ce and cs <= ne:
12                ns = min(ns, cs)
13                ne = max(ne, ce)
14            
15            elif ne < cs:
16                ans.append([ns,ne])
17                return ans + intervals[i:]
18            
19            elif ns > ce:
20                ans.append([cs,ce])
21
22            i += 1
23
24        ans.append([ns,ne])
25        return ans