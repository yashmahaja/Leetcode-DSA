# Last updated: 2/15/2026, 3:48:27 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        
4
5        intervals.sort()
6
7        c = 0
8
9        i = 0
10        j = 1
11        while j < len(intervals):
12            ps,pe = intervals[i]
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