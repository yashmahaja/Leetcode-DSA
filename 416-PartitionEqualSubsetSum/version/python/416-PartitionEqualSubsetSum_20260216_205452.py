# Last updated: 2/16/2026, 8:54:52 PM
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
16                return True
17
18            if suma < 0:
19                return False
20
21            take = 0  
22            if suma >= 0:
23                take = rec(i+1,suma - nums[i])
24
25            nt = rec(i+1, suma)
26
27            dp[i][suma] = (take or nt)
28            return dp[i][suma]
29
30        return rec(0, sum(nums) // 2)