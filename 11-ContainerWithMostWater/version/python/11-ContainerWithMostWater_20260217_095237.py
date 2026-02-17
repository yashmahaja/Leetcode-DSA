# Last updated: 2/17/2026, 9:52:37 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        
4
5        maxi = 0
6        l = 0
7        r = len(height) - 1
8        while l < r:
9            width = r - l
10            maxi = max(maxi, width * min(height[l], height[r]))
11            
12            if height[l] > height[r]:
13                r -= 1
14            else:
15                l += 1
16                
17        return maxi