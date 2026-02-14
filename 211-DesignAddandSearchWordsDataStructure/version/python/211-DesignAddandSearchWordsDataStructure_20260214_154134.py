# Last updated: 2/14/2026, 3:41:34 PM
1class Trie:
2
3    def __init__(self):
4        self.children = {}
5        self.w = False
6
7class WordDictionary:
8
9    def __init__(self):
10        self.root = Trie()
11
12    def addWord(self, word: str) -> None:
13        curr = self.root
14        for c in word:
15            if c not in curr.children:
16                curr.children[c] = Trie()
17            
18            curr = curr.children[c]
19        
20        curr.w = True
21
22    def search(self, word: str) -> bool:
23        curr = self.root
24
25        def dfs(idx,curr):
26            if idx == len(word):
27                return curr.w
28            
29            if word[idx] == ".":
30                for c in curr.children.values():
31                    if dfs(idx + 1, c):
32                        return True    
33                return False
34
35            else:
36                if word[idx] not in curr.children:
37                    return False
38                return dfs(idx+1, curr.children[word[idx]]) 
39
40        return dfs(0, curr)
41        
42
43
44# Your WordDictionary object will be instantiated and called as such:
45# obj = WordDictionary()
46# obj.addWord(word)
47# param_2 = obj.search(word)