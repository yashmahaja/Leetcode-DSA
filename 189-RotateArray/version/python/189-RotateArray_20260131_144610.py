# Last updated: 1/31/2026, 2:46:10 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k = k % len(nums)
7        def rev(st, end):
8            while st < end:
9                nums[st], nums[end] = nums[end], nums[st]
10
11                st += 1
12                end -= 1
13        
14
15        rev(0, len(nums)- 1)
16        rev(0, k - 1)
17        rev(k, len(nums) - 1)
18
19