# Last updated: 2/17/2026, 3:51:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        nn = h = ListNode()
10        carry = 0
11        while l1 or l2 or carry:
12            add = 0
13            if l1:
14                add += l1.val
15                l1  = l1.next
16            if l2:
17                add += l2.val
18                l2 = l2.next
19
20            add += carry
21            number = add % 10
22            carry = add // 10
23            h.next = ListNode(number)
24            h = h.next
25        
26        return nn.next