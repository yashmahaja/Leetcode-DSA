# Last updated: 2/17/2026, 10:38:49 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        if k == 1:
4            return nums
5        
6        # Go through the array one by one and as soon as r >= k - 1 we need to ans.append(q.popleft())
7        # As we go we'll check if nums[q[-1]] < nums[r] then q.pop()
8
9        if not k or not nums:
10            return []
11
12        ans = []
13        q = deque()
14        for r in range(len(nums)):
15
16            while q and nums[q[-1]] <= nums[r]:
17                q.pop()
18            
19            q.append(r)
20            
21            while q and not (r - k + 1 <= q[0] <= r):  
22                q.popleft()
23
24            if r >= k - 1:
25                ans.append(nums[q[0]])
26            
27        return ans
28        
29
30