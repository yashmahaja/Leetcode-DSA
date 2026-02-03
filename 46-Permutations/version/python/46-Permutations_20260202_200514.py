# Last updated: 2/2/2026, 8:05:14 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        
4
5        ans = []
6        cs = set()
7        def helper(temp):
8            if len(temp) == len(nums):
9                ans.append(temp.copy())
10                return
11            
12            for x in range(len(nums)):
13                if nums[x] not in temp:
14                    cs.add(nums[x])
15                    temp.append(nums[x])
16                    helper(temp)  
17                    temp.pop() 
18                    cs.remove(nums[x])
19
20        helper([])
21        return ans