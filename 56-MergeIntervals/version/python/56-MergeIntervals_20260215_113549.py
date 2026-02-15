# Last updated: 2/15/2026, 11:35:49 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        
4
5        ans  = []
6        intervals.sort()
7        ps, pe = intervals[0]
8        i = 1
9
10        while i < len(intervals):
11            cs,ce = intervals[i]
12
13            if cs <= pe:
14                ps = min(ps,cs)
15                pe = max(pe,ce)
16            
17            elif pe < cs:
18                ans.append([ps,pe])
19                ps = cs
20                pe = ce
21            
22            elif ps > ce:
23                ans.append([cs,ce])
24            
25            i += 1
26        
27        ans.append([ps,pe])
28        return ans