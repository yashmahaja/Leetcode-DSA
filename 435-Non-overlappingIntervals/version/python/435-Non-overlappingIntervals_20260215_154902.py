# Last updated: 2/15/2026, 3:49:02 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        
4        intervals.sort()
5        i = 0
6        j = 1
7        c = 0
8
9        while j < len(intervals):
10            ps, pe = intervals[i]
11            cs,ce = intervals[j]
12
13            if cs >= pe:
14                i = j
15                j += 1
16            
17            elif pe <= ce:
18                j += 1
19                c += 1
20            
21            elif pe > ce:
22                i = j
23                j += 1
24                c += 1
25            
26        return c