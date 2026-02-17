# Last updated: 2/17/2026, 10:01:29 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        #      [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
5        #         0  1  2  3  4  5  6  7  8  9  10  11
6        # maxl = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
7        # maxr = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0
8        
9        n = len(height)
10        l = 0
11        r = n - 1
12        lmax = height[0]
13        rmax = height[n-1]
14        trap = 0
15        while l < r:
16            if lmax <= rmax:
17                trap += lmax - height[l]
18                l += 1
19                lmax = max(lmax, height[l])
20            else:
21                trap += rmax - height[r]
22                r -= 1
23                rmax = max(rmax, height[r])
24        
25        return trap
26                
27
28
29
30       