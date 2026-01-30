# Last updated: 1/29/2026, 9:11:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        
11        if not p or not q or not root:
12            return root
13        
14        if max(p.val, q.val) < root.val:
15            return self.lowestCommonAncestor(root.left, p, q)
16        
17        elif min(p.val, q.val) > root.val:
18            return self.lowestCommonAncestor(root.right, p, q)
19        
20        else:
21            return root