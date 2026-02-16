# Last updated: 2/16/2026, 3:54:55 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4
5        pre = 1
6        pos = 1
7        ans = [1] * len(nums)
8        
9        for i in range(len(nums)):
10            ans[i] = pre
11            pre *= nums[i]
12        
13
14        for i in range(len(nums)):
15            j = -i - 1
16            
17            ans[j] *= pos
18            pos *= nums[j]
19    
20
21        return ans
22