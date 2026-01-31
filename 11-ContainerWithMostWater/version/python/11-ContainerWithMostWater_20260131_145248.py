# Last updated: 1/31/2026, 2:52:48 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        
4
5        l = 0
6        r = len(height) - 1
7        res = 0
8
9        while l < r:
10            res =  max(res, (r - l) * min(height[l], height[r]))
11
12            if height[l] < height[r]:
13                l += 1
14            else:
15                r -= 1
16        
17        return res