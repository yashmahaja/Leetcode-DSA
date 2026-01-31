# Last updated: 1/31/2026, 12:26:54 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        
4
5        intervals.sort()
6
7        i = 0
8        j = 1
9        c = 0
10
11        while j < len(intervals):
12            ps, pe = intervals[i]
13            cs, ce = intervals[j]
14
15            if cs >= pe:
16                i = j 
17                j += 1
18            
19            elif pe <= ce:
20                j += 1
21                c += 1
22            
23            elif pe >= ce:
24                i = j
25                j += 1
26                c += 1
27        
28        return c