# Last updated: 2/17/2026, 3:21:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        h = list1
10        n = list2
11
12        q = ListNode()
13        curr = q
14
15        while h is not None and n is not None:
16            if h.val < n.val:
17                q.next = h
18                h = h.next
19                q = q.next
20            else:
21                q.next = n
22                n = n.next
23                q = q.next
24        
25        if h:
26            q.next = h
27        if n:
28            q.next = n
29        
30        return curr.next
31
32