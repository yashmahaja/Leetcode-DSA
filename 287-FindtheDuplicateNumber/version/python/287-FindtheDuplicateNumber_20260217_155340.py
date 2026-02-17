# Last updated: 2/17/2026, 3:53:40 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        
4        slow = fast = 0
5        while True:
6            slow = nums[slow]
7            fast = nums[nums[fast]]
8
9            if slow == fast:
10                break
11
12        slow2 = 0
13        while slow != slow2:
14            slow = nums[slow]
15            slow2 = nums[slow2]
16
17        return slow 