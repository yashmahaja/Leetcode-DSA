# Last updated: 2/16/2026, 6:40:05 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        
4        dp = [-1] * (len(nums) + 1)
5
6        def rec(i):
7            if i >= len(nums):
8                return 0
9
10            if dp[i] != -1:
11                return dp[i]    
12
13            l = nums[i] + rec(i+2)
14            r = rec(i+1)
15
16            dp[i] =  max(l,r)
17            return dp[i]
18            
19        return rec(0)