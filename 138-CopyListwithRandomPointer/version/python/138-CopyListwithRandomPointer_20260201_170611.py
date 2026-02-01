# Last updated: 2/1/2026, 5:06:11 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        curr = head
13        store = {None: None}
14
15        while curr:
16            store[curr] = ListNode(curr.val)
17            curr = curr.next
18        
19        curr = head
20        while curr:
21            store[curr].next = store[curr.next]
22            store[curr].random = store[curr.random]
23            curr = curr.next
24        
25        return store[head]