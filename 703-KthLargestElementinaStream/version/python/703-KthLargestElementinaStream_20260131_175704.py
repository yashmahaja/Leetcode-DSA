# Last updated: 1/31/2026, 5:57:04 PM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.nums = nums
5        self.k = k
6        heapq.heapify(self.nums)
7        while len(self.nums) > self.k:
8            heapq.heappop(self.nums)
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.nums, val)
12        if len(self.nums) > self.k:
13            heapq.heappop(self.nums)
14        
15        return self.nums[0]
16# Your KthLargest object will be instantiated and called as such:
17# obj = KthLargest(k, nums)
18# param_1 = obj.add(val)