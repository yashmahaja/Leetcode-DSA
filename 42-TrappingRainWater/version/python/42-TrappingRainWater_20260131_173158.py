# Last updated: 1/31/2026, 5:31:58 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        #      [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
5        #         0  1  2  3  4  5  6  7  8  9  10  11
6        # maxl = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
7        # maxr = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0
8        
9        
10        maxl = [0] * len(height)
11        maxr = [0] * len(height)
12        l = 0
13        r = 0
14        for x in range(len(height)):
15            j = -x - 1
16
17            maxl[x] = l
18            l = max(l, height[x])
19
20            maxr[j] = r
21            r = max(r, height[j])
22        
23        trap = 0
24        for x, val in enumerate(height):
25            trap += max(0, min(maxl[x],maxr[x]) - height[x])
26        
27        return trap