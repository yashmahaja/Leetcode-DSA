# Last updated: 2/17/2026, 4:15:12 PM
1class Node:
2    def __init__(self, key,  value):
3        self.key = key
4        self.value =  value
5        self.prev = None
6        self.next = None
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.cap = capacity
12        self.cache = {}
13        self.right = Node(0,0)
14        self.left = Node(0,0)
15        self.right.prev = self.left
16        self.left.next = self.right
17    
18    def insert(self,node):
19        prev , nxt = self.right.prev, self.right
20        prev.next = node
21        nxt.prev = node
22        node.next = nxt
23        node.prev = prev
24
25        
26    def remove(self,node):
27        prev, nxt = node.prev, node.next
28        prev.next = nxt
29        nxt.prev = prev
30
31
32    def get(self, key: int) -> int:
33
34        if key not in self.cache:
35            return -1
36
37        self.remove(self.cache[key])
38        self.insert(self.cache[key])
39        return self.cache[key].value
40        
41
42    def put(self, key: int, value: int) -> None:
43        if key in self.cache:
44            self.remove(self.cache[key])
45        
46        self.cache[key] = Node(key,value)
47        self.insert(self.cache[key])
48        if len(self.cache) > self.cap:
49            lru = self.left.next
50            self.remove(lru)
51            del self.cache[lru.key]
52
53
54
55# Your LRUCache object will be instantiated and called as such:
56# obj = LRUCache(capacity)
57# param_1 = obj.get(key)
58# obj.put(key,value)