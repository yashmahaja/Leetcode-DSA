# Last updated: 2/2/2026, 4:16:59 PM
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
11
12        for i, node in enumerate(lists):
13            if node:
14                heapq.heappush(h, (node.val, i,  node))
15
16        res = ListNode()
17        curr = res
18
19        while h:
20            value, i, node = heapq.heappop(h)
21            curr.next = node
22            curr = curr.next
23            if node.next != None:
24                heapq.heappush(h, (node.next.val, i, node.next))
25
26        return res.next