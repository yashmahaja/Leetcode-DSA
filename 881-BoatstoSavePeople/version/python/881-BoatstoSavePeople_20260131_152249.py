# Last updated: 1/31/2026, 3:22:49 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        
4
5        i = 0 
6        people.sort()
7
8        j = len(people) - 1
9        b = 0
10
11        while i <= j:
12
13            if people[i] + people[j] <= limit:
14                i += 1
15            
16            j -= 1
17            b += 1
18        
19        return b