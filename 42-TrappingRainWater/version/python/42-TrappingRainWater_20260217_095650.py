# Last updated: 2/17/2026, 9:56:50 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        #      [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
5        #         0  1  2  3  4  5  6  7  8  9  10  11
6        # maxl = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
7        # maxr = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0
8        
9        pre = [0] * len(height)
10        pos = [0] * len(height)
11        l = 0
12        r = 0
13        for i in range(len(height)):
14            pre[i] = l
15            l = max(l, height[i])
16        
17        for j in range(len(height) - 1, -1, -1):
18            pos[j] = r
19            r = max(r, height[j])
20        
21        
22        trap = 0
23        for x in range(len(height)):
24            trap += max(0,min(pre[x],pos[x]) - height[x])
25        
26        return trap