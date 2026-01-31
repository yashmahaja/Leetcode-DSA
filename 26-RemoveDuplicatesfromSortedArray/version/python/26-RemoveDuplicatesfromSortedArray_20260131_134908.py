# Last updated: 1/31/2026, 1:49:08 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        
4
5        d = 0
6        for i in range(len(nums)):
7            if nums[d] != nums[i]:
8                d += 1
9                nums[d] = nums[i]
10
11        return d + 1