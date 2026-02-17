# Last updated: 2/17/2026, 11:37:56 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        
4        fleet = sorted(zip(position,speed), reverse=True)
5        
6        s = []
7        c = 0
8        for pos, sp in fleet:
9            time = (target - pos ) / sp
10            if not s or s[-1] < time:
11                s.append(time)
12            
13        return len(s)
14        