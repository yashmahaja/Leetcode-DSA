# Last updated: 1/31/2026, 2:18:43 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        
4        nums.sort()
5
6        res = []
7
8        for i in range(len(nums)):
9            if i > 0 and nums[i] == nums[i-1]:
10                continue
11            
12            j = i + 1
13            k = len(nums) - 1
14
15            while j < k:
16                add = nums[i] + nums[j] + nums[k]
17                if add == 0:
18                    res.append([nums[i], nums[j], nums[k]])
19
20                    j += 1
21                    k -= 1
22
23                    while j < k and nums[j] == nums[j-1]:
24                        j += 1
25                    
26                    while j < k and nums[k] == nums[k+1]:
27                        k -= 1
28                    
29                elif add > 0:
30                    k -= 1
31                
32                else:
33                    j += 1
34            
35        return res
36         