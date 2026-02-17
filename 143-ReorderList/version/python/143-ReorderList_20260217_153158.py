# Last updated: 2/17/2026, 3:31:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        curr = head
12
13        slow = fast = curr
14
15        while fast != None and fast.next != None:
16            slow = slow.next
17            fast = fast.next.next
18
19        prev = None
20        slow1 = slow
21        while slow:
22            temp = slow.next
23            slow.next = prev
24            prev = slow
25            slow = temp
26        
27        while prev.next != None:
28            temp = curr.next
29            curr.next = prev
30            curr = temp
31
32            temp1 = prev.next
33            prev.next = curr
34            prev = temp1
35
36        return head
37            