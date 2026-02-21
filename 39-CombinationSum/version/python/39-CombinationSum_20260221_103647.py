# Last updated: 2/21/2026, 10:36:47 AM
1class Solution:
2    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
3        
4        ans = []
5        def rec(i,add, temp):
6            if add == target:
7                ans.append(temp[:])
8                return
9
10            if i >= len(c) or add > target:
11                return 
12
13            for x in range(i, len(c)):
14                if add + c[x] <= target:
15                    temp.append(c[x])
16                    rec(x, add + c[x], temp)
17                    temp.pop()
18
19        rec(0,0,[])
20        return ans