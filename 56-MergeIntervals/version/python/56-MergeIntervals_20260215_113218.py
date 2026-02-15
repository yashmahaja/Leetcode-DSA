# Last updated: 2/15/2026, 11:32:18 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        
4
5        ans  = []
6        intervals.sort()
7        cs, ce = intervals[0]
8        i = 1
9
10        while i < len(intervals):
11            ns,ne = intervals[i]
12
13            if ns <= ce:
14                cs = min(ns,cs)
15                ce = max(ne,ce)
16            
17            elif ce < ns:
18                ans.append([cs,ce])
19                cs = ns
20                ce = ne
21            
22            elif ce > ns:
23                ans.append([ns,ne])
24            
25            i += 1
26        
27        ans.append([cs,ce])
28        return ans