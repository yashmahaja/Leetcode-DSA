# Last updated: 2/16/2026, 9:37:42 AM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        
4        pre = 1
5        pos = 1
6        maxi = float("-inf")
7
8        for i, x in enumerate(nums):
9            j = -i - 1
10
11            if pre == 0:
12                pre = 1
13            
14            if pos == 0:
15                pos = 1
16            
17
18            pre *= nums[i]
19            pos *= nums[j]
20
21            maxi = max(maxi, max(pre,pos))
22            print(maxi)
23        
24        return maxi
25