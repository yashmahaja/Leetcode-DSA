# Last updated: 2/14/2026, 1:14:16 PM
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
13        root.w = True
14
15    def search(self, word: str) -> bool:
16        root = self
17        for c in word:
18            if c not in root.children:
19                return False
20            root = root.children[c]
21        return root.w
22
23    def startsWith(self, prefix: str) -> bool:
24        root = self
25        for c in prefix:
26            if c not in root.children:
27                return False
28            root = root.children[c]
29        
30        return True
31
32
33# Your Trie object will be instantiated and called as such:
34# obj = Trie()
35# obj.insert(word)
36# param_2 = obj.search(word)
37# param_3 = obj.startsWith(prefix)