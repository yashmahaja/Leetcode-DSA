# Last updated: 2/17/2026, 12:31:35 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4
5        l = 0
6        r = len(nums) - 1
7
8        while l <= r:
9            mid = (l + r) // 2
10            if nums[mid] == target:
11                return mid
12            
13            if nums[mid] >= nums[l]:
14                if nums[l] <= target < nums[mid]:
15                    r = mid - 1
16                else:
17                    l = mid + 1
18            else:
19                if nums[mid] < target <= nums[r]:
20                    l = mid + 1
21                else:
22                    r = mid - 1
23
24        return -1 