# Last updated: 2/17/2026, 11:28:58 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        
4
5        s = []
6        t = temperatures
7        ans = [0] * len(t)
8        for x in range(len(temperatures)):
9
10            while s and t[s[-1]] < t[x]:
11                j = s.pop()
12                ans[j] = x -  j
13            
14            s.append(x)
15        
16        return ans