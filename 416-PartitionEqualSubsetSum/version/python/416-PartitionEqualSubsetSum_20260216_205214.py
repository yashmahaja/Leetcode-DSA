# Last updated: 2/16/2026, 8:52:14 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        
4        if sum(nums) % 2 != 0:
5            return False
6        
7        dp = [[None] * (sum(nums) // 2 + 1) for i in range(len(nums))]
8        def rec(i, suma):
9            if i >= len(nums):
10                return False
11
12            if dp[i][suma] is not None:
13                return dp[i][suma]
14
15            if suma == 0:
16                dp[i][suma] =  True
17                return True
18
19            if suma < 0:
20                dp[i][suma] =  False
21                return False
22
23            take = 0  
24            if suma >= 0:
25                take = rec(i+1,suma - nums[i])
26
27            nt = rec(i+1, suma)
28
29            dp[i][suma] = (take or nt)
30            return dp[i][suma]
31
32        return rec(0, sum(nums) // 2)