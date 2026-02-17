# Last updated: 2/17/2026, 11:46:44 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        
4
5        # nse 
6        # pse
7        # need to get => (nse - pse - 1) * heights[curr]
8
9        nse = [len(heights)] * len(heights)
10        pse = [-1] * len(heights)
11        s = []
12        for x in range(len(heights)):
13            while s and heights[s[-1]] > heights[x]:
14                j = s.pop()
15                nse[j] = x
16            
17            s.append(x)
18        
19        s = []
20        for x in range(len(heights) - 1, -1, -1):
21            while s and heights[s[-1]] > heights[x]:
22                j = s.pop()
23                pse[j] = x
24            
25            s.append(x)
26       
27        maxi = 0
28        for i in range(len(heights)):
29            maxi = max(maxi, (nse[i] - pse[i] - 1 ) * heights[i])
30        
31        return maxi
32            
33
34