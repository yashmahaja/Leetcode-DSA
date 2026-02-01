# Last updated: 2/1/2026, 12:56:23 PM
1class WordDictionary:
2    def __init__(self):
3        self.children = {}
4        self.word = False
5
6    def addWord(self, word: str) -> None:
7        curr = self
8        for c in word:
9            if c not  in curr.children:
10               curr.children[c] = WordDictionary()
11            curr = curr.children[c]  
12        curr.word = True 
13
14    def search(self, word: str) -> bool:
15        root = self
16        def dfs(i, root):
17            if i == len(word):
18                return root.word
19            
20            if word[i] == ".":
21                for l in root.children.values():
22                    if dfs(i+1, l):
23                        return True
24                return False
25            else:
26                if word[i] not in root.children:
27                    return False
28                return dfs(i+1, root.children[word[i]])
29
30        return dfs(0,root)
31
32
33# Your WordDictionary object will be instantiated and called as such:
34# obj = WordDictionary()
35# obj.addWord(word)
36# param_2 = obj.search(word)