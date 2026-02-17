# Last updated: 2/17/2026, 12:15:28 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        
4
5
6        def speed(ps):
7            add = 0
8            for x in piles:
9                add += math.ceil(x / ps)
10
11            return add <= h
12
13        l = 1
14        r = max(piles)
15
16        while l < r:
17            mid = ( l + r ) // 2
18            if speed(mid):
19                r = mid
20            else:
21                l = mid + 1
22        
23        return l
24