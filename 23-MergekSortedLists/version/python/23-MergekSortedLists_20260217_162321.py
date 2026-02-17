# Last updated: 2/17/2026, 4:23:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        
9
10        h = []
11        for i, x in enumerate(lists):
12            if x:
13                heapq.heappush(h, (x.val, i, x))
14
15        curr = ListNode()
16        res = curr
17
18        while h:
19            value, idx, node = heapq.heappop(h)
20            res.next = node
21            res = res.next
22            if node.next != None:
23                heapq.heappush(h,(node.next.val,idx, node.next))
24        
25        return curr.next