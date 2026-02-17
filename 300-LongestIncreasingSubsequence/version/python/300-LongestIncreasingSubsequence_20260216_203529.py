# Last updated: 2/16/2026, 8:35:29 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        
4        dp =[[-1] * len(nums) for i in range(len(nums))]
5        def rec(prev, curr):
6            if curr >= len(nums):
7                return 0
8            
9            if dp[prev][curr] != -1:
10                return dp[prev][curr]
11
12            take = 0
13            if prev == -1 or nums[curr] > nums[prev]:
14                take = 1 + rec(curr, curr+1)
15            
16            nt = rec(prev, curr+1)
17
18            dp[prev][curr] =  max(take,nt)
19            return dp[prev][curr]
20        
21
22        return rec(-1, 0)