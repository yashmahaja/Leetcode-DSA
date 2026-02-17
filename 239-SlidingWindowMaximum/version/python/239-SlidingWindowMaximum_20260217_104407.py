# Last updated: 2/17/2026, 10:44:07 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        
4
5
6        q = deque()
7        ans = []
8        for r in range(len(nums)):
9
10            while q and nums[q[-1]] <= nums[r]:
11                q.pop()
12            
13            q.append(r)
14
15            while q and not (r - k + 1 <= q[0] <= r):
16                q.popleft()
17
18            if r >= k - 1:
19                ans.append(nums[q[0]])
20        
21        return ans
22