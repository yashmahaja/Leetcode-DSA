# Last updated: 2/17/2026, 3:24:49 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        
10
11        curr = head
12        slow = fast = curr
13
14        while fast is not None and fast.next is not None:
15            slow = slow.next
16            fast = fast.next.next
17
18            if slow == fast:
19                return True
20        
21        return False