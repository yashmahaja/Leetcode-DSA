# Last updated: 2/17/2026, 12:21:18 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        
4
5        l = 0
6        r = len(nums) - 1
7
8        while l < r:
9            mid = (l + r ) // 2
10            if nums[mid] > nums[r]:
11                l = mid + 1
12            else:
13                r = mid
14        
15        return nums[l]