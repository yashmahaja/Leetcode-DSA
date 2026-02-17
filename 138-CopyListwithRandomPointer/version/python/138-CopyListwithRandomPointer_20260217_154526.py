# Last updated: 2/17/2026, 3:45:26 PM
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
12        store = {None : None}
13
14        curr = head
15
16        while curr:
17            store[curr] = Node(curr.val)
18            curr = curr.next
19        
20        curr = head
21        while curr:
22            store[curr].next = store[curr.next]
23            store[curr].random = store[curr.random]
24            curr = curr.next
25        
26        return store[head]