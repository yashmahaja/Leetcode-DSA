# Last updated: 2/2/2026, 7:54:58 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        
4        ans = []
5        candidates.sort()
6        
7        def helper(i, add ,t):
8            if add == target:
9                ans.append(t[:])
10                return
11            
12            if i >= len(candidates) and add > target:
13                return
14
15            for x in range(i, len(candidates)):
16                if x > i and candidates[x] == candidates[x-1]:
17                    continue
18                if add + candidates[x] <= target:
19                    t.append(candidates[x])
20                    helper(x+1, add + candidates[x], t)
21                    t.pop()            
22
23        helper(0, 0, [])
24        return ans