# Last updated: 2/14/2026, 10:17:43 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.nums = nums
5        self.k = k
6        heapq.heapify(self.nums)
7
8        while len(self.nums) > self.k:
9            heapq.heappop(self.nums)
10
11    def add(self, val: int) -> int:
12        heapq.heappush(self.nums, val)
13        if len(self.nums) > self.k:
14            heapq.heappop(self.nums)
15
16        return self.nums[0]
17
18# Your KthLargest object will be instantiated and called as such:
19# obj = KthLargest(k, nums)
20# param_1 = obj.add(val)