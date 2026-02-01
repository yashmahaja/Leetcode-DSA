# Last updated: 2/1/2026, 5:23:35 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        
4
5        s = f = 0
6        while True:
7            s = nums[s]
8            f = nums[nums[f]]
9
10            if f == s:
11                break
12        
13        s2 = 0
14        while s != s2:
15            s = nums[s]
16            s2 = nums[s2]
17        
18        return s