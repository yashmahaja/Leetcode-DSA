# Last updated: 2/3/2026, 10:03:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9
10
11        q = deque([root])
12        maxs = float("-inf")
13        maxl = -1
14        currl = 1
15        while q:
16            level = 0
17            for i in range(len(q)):
18                curr = q.popleft()
19                level += curr.val
20                if curr.left:
21                    q.append(curr.left)
22                if curr.right:
23                    q.append(curr.right)
24            
25            if maxs < level:
26                    maxs = level
27                    maxl = currl
28
29            currl += 1
30        return maxl