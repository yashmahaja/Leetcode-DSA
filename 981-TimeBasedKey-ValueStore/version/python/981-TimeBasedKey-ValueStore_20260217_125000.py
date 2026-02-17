# Last updated: 2/17/2026, 12:50:00 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.store:
8            self.store[key] = []
9        self.store[key].append((value, timestamp))
10
11    def get(self, key: str, timestamp: int) -> str:
12        values = self.store.get(key, [])
13        res = ""
14        l = 0 
15        r = len(values) - 1
16        while l <= r:
17            mid = (l + r) // 2
18            if values[mid][1] <= timestamp:
19                res = values[mid][0]
20                l = mid + 1
21            else:
22                r = mid - 1
23        
24        return res
25    
26        
27
28# Your TimeMap object will be instantiated and called as such:
29# obj = TimeMap()
30# obj.set(key,value,timestamp)
31# param_2 = obj.get(key,timestamp)