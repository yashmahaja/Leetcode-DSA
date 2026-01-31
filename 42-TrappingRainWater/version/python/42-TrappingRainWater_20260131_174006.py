# Last updated: 1/31/2026, 5:40:06 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        #      [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
5        #         0  1  2  3  4  5  6  7  8  9  10  11
6        # maxl = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
7        # maxr = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0
8        
9        
10        l = 0
11        r = len(height) - 1
12        lmax = height[l]
13        rmax = height[r]
14
15        trap = 0
16
17        while l < r:
18            if lmax <= rmax:
19                trap += lmax - height[l]
20                l += 1
21                lmax = max(height[l], lmax)
22            else:
23                trap += rmax - height[r]
24                r -= 1
25                rmax = max(height[r], rmax)
26        
27        return trap