# Last updated: 2/16/2026, 3:45:50 AM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        ans = []
6        for x in strs:
7            ans.append(str(len(x)) + "$" + x)
8        
9        return "".join(ans)
10
11    def decode(self, s: str) -> List[str]:
12        """Decodes a single string to a list of strings.
13        """
14        i = 0
15        res = []
16        while i < len(s):
17            j = i + 1
18
19            while s[j] != "$":
20                j += 1
21            
22            l = int(s[i:j])
23            res.append(s[j+1: j + 1 + l])
24
25            i = j + 1 + l
26        
27        return res
28        
29
30
31# Your Codec object will be instantiated and called as such:
32# codec = Codec()
33# codec.decode(codec.encode(strs))