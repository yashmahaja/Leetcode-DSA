# Last updated: 2/17/2026, 3:14:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9
10        prev = None
11        curr = head
12        while curr:
13            temp = curr.next
14            curr.next = prev
15            prev =  curr
16            curr = temp
17        
18        return prev