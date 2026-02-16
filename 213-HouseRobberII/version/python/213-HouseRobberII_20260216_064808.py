# Last updated: 2/16/2026, 6:48:08 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        
4        dp = [[-1] * len(nums) for i in range(len(nums))]
5        if len(nums) == 1:
6            return nums[0]
7  
8        def solve(i,end):
9            if i > end:
10                return 0
11        
12            if dp[i][end] != -1:
13                return dp[i][end]
14
15            l = nums[i] + solve(i + 2, end)
16            r = solve(i + 1, end)
17
18            dp[i][end] =  max(l,r)
19            return dp[i][end]
20
21        l = solve(0, len(nums) - 2)
22        r = solve(1, len(nums) - 1)
23        return max(l,r)