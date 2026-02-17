# Last updated: 2/17/2026, 12:10:57 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3
4        m = len(matrix)
5        n = len(matrix[0])
6
7        l = 0
8        r = m * n - 1
9
10        while l <= r:
11            mid = (l + r) // 2
12            if matrix[mid // n][mid % n] == target:
13                return True
14            elif matrix[mid // n][mid % n] > target:
15                r -= 1
16            else:
17                l += 1
18        
19        return False