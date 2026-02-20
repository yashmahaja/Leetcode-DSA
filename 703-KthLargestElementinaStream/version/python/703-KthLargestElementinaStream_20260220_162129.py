# Last updated: 2/20/2026, 4:21:29 PM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.nums = nums
5        self.k = k
6
7        heapq.heapify(self.nums)
8        while len(self.nums) > k:
9            heapq.heappop(self.nums)
10
11
12    def add(self, val: int) -> int:
13        heapq.heappush(self.nums, val)
14        while len(self.nums) > self.k:
15            heapq.heappop(self.nums)
16        
17        return self.nums[0]
18
19
20# Your KthLargest object will be instantiated and called as such:
21# obj = KthLargest(k, nums)
22# param_1 = obj.add(val)