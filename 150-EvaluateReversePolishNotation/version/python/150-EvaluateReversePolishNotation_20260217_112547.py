# Last updated: 2/17/2026, 11:25:47 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        
4        s = []
5        for x in tokens:
6            if x == "+":
7                second = s.pop()
8                first = s.pop()
9                s.append(second + first)
10            
11            elif x == "-":
12                second = s.pop()
13                first = s.pop()
14                s.append(first - second)
15            
16            elif x == "/":
17                second = s.pop()
18                first = s.pop()
19                s.append(int(first / second))
20            
21            elif x == "*":
22                second = s.pop()
23                first = s.pop()
24                s.append(second * first)
25            
26            else:
27                s.append(int(x))
28        
29        return s[0]