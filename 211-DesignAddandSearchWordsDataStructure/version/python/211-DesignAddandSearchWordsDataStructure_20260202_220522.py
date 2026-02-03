# Last updated: 2/2/2026, 10:05:22 PM
1class Trie:
2    def __init__(self):
3        self.child = {}
4        self.w = False
5
6class WordDictionary:
7
8    def __init__(self):
9        self.root = Trie()
10
11    def addWord(self, word: str) -> None:
12        curr = self.root
13        for c in word:
14            if c not in curr.child:
15                curr.child[c] = Trie()
16            curr = curr.child[c]
17        curr.w = True
18
19    def search(self, word: str) -> bool:
20        curr = self.root
21        def dfs(x, curr):
22           
23            if x == len(word):
24                return curr.w
25           
26            if word[x] == ".":
27                
28                for val in curr.child.values():
29                    if  dfs(x+1, val):
30                        return True                        
31                return False
32
33            elif word[x] != ".":
34                if word[x] not in curr.child:
35                    return False
36                return dfs(x+1, curr.child[word[x]])
37        
38        return dfs(0, curr)
39
40
41
42
43
44# Your WordDictionary object will be instantiated and called as such:
45# obj = WordDictionary()
46# obj.addWord(word)
47# param_2 = obj.search(word)