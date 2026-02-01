# Last updated: 2/1/2026, 4:59:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        
9        i = 0
10        curr = head
11
12        while curr:
13            curr = curr.next
14            i += 1
15        
16        curr = head
17        if n == i:
18            return curr.next
19
20
21        j = 0
22        while j < i - n - 1:
23            curr = curr.next
24            j += 1
25        
26        curr.next = curr.next.next
27        return head
28