# Last updated: 2/1/2026, 4:53:19 PM
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
11
12
13        slow = fast = head
14
15        while fast != None and fast.next != None:
16            slow = slow.next
17            fast = fast.next.next
18        
19        prev = None
20        curr = slow
21        while curr:
22            temp = curr.next
23            curr.next = prev
24            prev = curr
25            curr = temp
26        
27    
28        h = head
29
30        while prev.next:
31            temp = h.next
32            h.next = prev
33            h = temp
34
35            t2 = prev.next
36            prev.next = h
37            prev = t2
38        
39        return head
40        
41
42
43        
44        