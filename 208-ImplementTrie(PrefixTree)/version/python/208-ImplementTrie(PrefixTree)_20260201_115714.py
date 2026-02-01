# Last updated: 2/1/2026, 11:57:14 AM
1class Trie:
2
3    def __init__(self):
4        self.children = {}
5        self.w = False
6
7    def insert(self, word: str) -> None:
8        root = self
9        for c in word:
10            if c not in root.children:
11                root.children[c] = Trie()    
12            root = root.children[c]
13        
14        root.w = True
15
16    def search(self, word: str) -> bool:
17        root = self
18        for c in word:
19            if c not in root.children:
20                return False
21            root = root.children[c]
22
23        return root.w
24
25    def startsWith(self, prefix: str) -> bool:
26        root = self
27        for c in prefix:
28            if c not in root.children:
29                return False
30            root = root.children[c]
31        return True
32
33
34# Your Trie object will be instantiated and called as such:
35# obj = Trie()
36# obj.insert(word)
37# param_2 = obj.search(word)
38# param_3 = obj.startsWith(prefix)