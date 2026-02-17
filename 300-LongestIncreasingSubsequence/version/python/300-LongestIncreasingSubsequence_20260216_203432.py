# Last updated: 2/16/2026, 8:34:32 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        
4        tails = []
5
6        def lower(arr, target):
7            l, r = 0, len(arr)
8            while l < r:
9                m = (l + r ) // 2
10                if arr[m] < target:
11                    l = m + 1
12                else:
13                    r = m
14
15            return l
16        
17
18        for x in nums:
19            idx = lower(tails, x)
20            if idx == len(tails):
21                tails.append(x)
22            else:
23                tails[idx] = x
24        
25        return len(tails)