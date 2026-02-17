# Last updated: 2/17/2026, 11:58:03 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        
4
5        # nse 
6        # pse
7        # need to get => (nse - pse - 1) * heights[curr]
8
9        s = []
10        maxi = float("-inf")
11        for x in range(len(heights) + 1):
12            ns = heights[x] if x < len(heights) else -1
13            while s and heights[s[-1]] > ns:
14                curr = s.pop()
15                prev = s[-1] if s else -1 
16                maxi = max(maxi,(x - prev - 1) * heights[curr])
17            
18            s.append(x)
19        
20        return maxi
21
22            
23
24