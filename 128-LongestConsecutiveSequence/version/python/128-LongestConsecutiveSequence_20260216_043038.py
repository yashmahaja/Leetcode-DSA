# Last updated: 2/16/2026, 4:30:38 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        
4        nums = set(nums)
5        maxi = 0
6        for x in nums:
7            if x - 1 in nums:
8                continue
9
10            l = 0
11            while x + l in nums:
12                l += 1
13
14            maxi = max(maxi, l)
15        
16        return maxi