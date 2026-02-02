# Last updated: 2/2/2026, 3:56:46 PM
1class Node:
2    def __init__(self, key, value):
3        self.key = key
4        self.value = value
5        self.prev = None
6        self.next = None
7
8
9class LRUCache:
10
11    def __init__(self, capacity: int):
12        self.cache = {}
13        self.capacity = capacity
14        self.left = Node(0,0)
15        self.right = Node(0,0)
16        self.left.next = self.right
17        self.right.prev = self.left
18
19
20    def insert(self, node):
21        prev, nxt = self.right.prev, self.right
22        prev.next = node
23        nxt.prev = node
24        node.prev = prev
25        node.next = nxt
26    
27    def remove(self, node):
28        prev, nxt = node.prev, node.next
29        prev.next = nxt
30        nxt.prev = prev
31
32
33    def get(self, key: int) -> int:
34        if key in self.cache:
35            self.remove(self.cache[key])
36            self.insert(self.cache[key])
37            return self.cache[key].value
38        return -1
39
40    def put(self, key: int, value: int) -> None:
41        if key in self.cache:
42            self.remove(self.cache[key])
43
44        self.cache[key] = Node(key, value)
45        self.insert(self.cache[key])
46        if self.capacity < len(self.cache):
47            lru = self.left.next
48            self.remove(lru)
49            del self.cache[lru.key]
50        
51
52
53# Your LRUCache object will be instantiated and called as such:
54# obj = LRUCache(capacity)
55# param_1 = obj.get(key)
56# obj.put(key,value)