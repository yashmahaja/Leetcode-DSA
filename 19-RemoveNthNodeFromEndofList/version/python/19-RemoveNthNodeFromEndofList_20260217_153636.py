# Last updated: 2/17/2026, 3:36:36 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        
9        curr = head
10        l = 0
11        while curr:
12            curr = curr.next
13            l += 1
14        
15        curr = head
16
17        if l == n:
18            return head.next
19            
20        for x in range(l - n - 1):
21            curr = curr.next
22        
23        curr.next = curr.next.next
24
25        return head
26