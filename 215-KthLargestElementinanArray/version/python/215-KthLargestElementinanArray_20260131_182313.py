# Last updated: 1/31/2026, 6:23:13 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        
4
5        h = []
6
7        for x in nums:
8            heapq.heappush(h, x)
9            if len(h) > k:
10                heapq.heappop(h)
11        
12        return h[0]