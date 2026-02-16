# Last updated: 2/16/2026, 6:45:28 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        if n == 1:
6            return nums[0]
7
8        dp = {}
9        def rec(i,k):
10            if i >= k:
11                return 0
12            if (i, k) in dp:
13                return dp[(i, k)]
14            take = nums[i] + rec(i+2,k)
15            nt = rec(i+1,k)
16            dp[(i, k)] = max(take,nt)
17            return dp[(i, k)]
18
19        return max(rec(0,n-1),rec(1,n))