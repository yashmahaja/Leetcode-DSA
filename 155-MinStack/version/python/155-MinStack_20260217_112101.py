# Last updated: 2/17/2026, 11:21:01 AM
1class MinStack:
2
3    def __init__(self):
4        self.s = []
5        self.ms = []
6
7    def push(self, val: int) -> None:
8        self.s.append(val)
9        if not self.ms or self.ms[-1] >= val:
10            self.ms.append(val)
11
12    def pop(self) -> None:
13        if self.s:
14            val = self.s.pop() 
15        if self.ms and self.ms[-1] ==  val:
16            self.ms.pop()
17
18    def top(self) -> int:
19        if self.s:
20            return self.s[-1]
21
22    def getMin(self) -> int:
23        if self.ms:
24            return self.ms[-1]
25
26
27# Your MinStack object will be instantiated and called as such:
28# obj = MinStack()
29# obj.push(val)
30# obj.pop()
31# param_3 = obj.top()
32# param_4 = obj.getMin()