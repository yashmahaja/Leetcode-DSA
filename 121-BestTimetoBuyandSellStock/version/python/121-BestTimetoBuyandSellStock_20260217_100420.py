# Last updated: 2/17/2026, 10:04:20 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        
4
5        maxi = 0
6        small = prices[0]
7
8        for i in range(1, len(prices)):
9            if prices[i] < small:
10                small = prices[i]
11            
12            maxi = max(maxi, prices[i] - small)
13        
14        return maxi
15
16        