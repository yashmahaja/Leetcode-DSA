# Last updated: 2/17/2026, 12:54:33 PM
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
15        r = len(values)
16        while l < r:
17            mid = (l + r) // 2
18            if values[mid][1] <= timestamp:
19                l = mid + 1
20            else:
21                r = mid
22        
23        idx = l - 1
24        return values[idx][0] if idx >= 0 else "" 
25    
26        
27
28# Your TimeMap object will be instantiated and called as such:
29# obj = TimeMap()
30# obj.set(key,value,timestamp)
31# param_2 = obj.get(key,timestamp)