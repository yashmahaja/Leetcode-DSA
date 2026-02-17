# Last updated: 2/17/2026, 9:49:37 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        
4        nums.sort()
5        ans = []
6        for idx, val in enumerate(nums):
7            if  idx > 0 and val == nums[idx - 1]:
8                continue
9            
10            j = idx + 1
11            k = len(nums) - 1
12            while j < k:
13                add = nums[idx] + nums[k] + nums[j]
14                if add == 0:
15                    ans.append([nums[idx], nums[j], nums[k]])
16
17                    j += 1
18                    k -= 1
19                    while j < k and nums[j] == nums[j-1]:
20                        j += 1
21                    
22                    while j < k and nums[k] == nums[k + 1]:
23                        k -= 1
24                    
25                elif add > 0:
26                    k -= 1
27                
28                else:
29                    j += 1
30            
31        return ans
32