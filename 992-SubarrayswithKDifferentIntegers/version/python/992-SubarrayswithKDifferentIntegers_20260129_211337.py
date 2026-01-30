# Last updated: 1/29/2026, 9:13:37 PM
1class Solution:
2    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
3         
4
5        def atmost(k):
6            l = 0
7            c = 0
8            maps = {}
9            for r in range(len(nums)):
10                maps[nums[r]] = 1 + maps.get(nums[r], 0)
11
12                while len(maps) > k:
13                    maps[nums[l]] -= 1
14                    if maps[nums[l]] == 0:
15                        del maps[nums[l]]
16                    l += 1
17                
18                c += r - l + 1
19
20            return c
21
22
23        return atmost(k) - atmost(k-1)