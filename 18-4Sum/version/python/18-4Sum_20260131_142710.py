# Last updated: 1/31/2026, 2:27:10 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        
4
5        res = []
6        nums.sort()
7
8        for r in range(len(nums)):
9            if r > 0 and nums[r] == nums[r - 1]:
10                continue
11            
12            for j in range(r + 1, len(nums)):
13                if j > r + 1 and nums[j] == nums[j-1]:
14                    continue
15            
16                k = j + 1
17                m = len(nums) - 1
18
19                while k < m:
20                    add = nums[r] + nums[j] + nums[k] + nums[m]
21
22                    if add == target:
23                        res.append([nums[r], nums[j], nums[k], nums[m]])
24
25                        k += 1
26                        m -= 1
27
28                        while k < m and nums[k] == nums[k-1]:
29                            k += 1
30                        
31                        while k < m and nums[m] == nums[m + 1]:
32                            m -= 1
33                        
34                    elif add > target:
35                        m -= 1
36                    
37                    else:
38                        k += 1
39                        
40        return res
41