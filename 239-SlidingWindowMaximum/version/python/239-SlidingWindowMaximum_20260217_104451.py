# Last updated: 2/17/2026, 10:44:51 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        
4        if k == 1:
5            return nums
6        
7        if not k and not nums:
8            return []
9
10
11        q = deque()
12        ans = []
13        for r in range(len(nums)):
14
15            while q and nums[q[-1]] <= nums[r]:
16                q.pop()
17            
18            q.append(r)
19
20            while q and not (r - k + 1 <= q[0] <= r):
21                q.popleft()
22
23            if r >= k - 1:
24                ans.append(nums[q[0]])
25        
26        return ans
27