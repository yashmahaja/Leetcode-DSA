# Last updated: 2/1/2026, 5:15:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8
9        nn = k  = ListNode()
10        carry = 0
11        
12        while l1 or l2 or carry:
13            res = 0
14            if l1:
15                res += l1.val
16                l1 = l1.next
17            
18            if l2:
19                res += l2.val
20                l2 = l2.next
21            
22            res += carry
23            n = res % 10 
24            carry = res // 10
25            nn.next = ListNode(n)
26            nn = nn.next
27        
28        return k.next