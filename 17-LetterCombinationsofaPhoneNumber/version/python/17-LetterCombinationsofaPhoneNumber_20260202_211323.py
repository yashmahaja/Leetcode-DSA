# Last updated: 2/2/2026, 9:13:23 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digitsToChar = {
4            '2':"abc",
5            '3':"def",
6            '4':"ghi",
7            '5':"jkl",
8            '6':"mno",
9            '7':"pqrs",
10            '8':"tuv",
11            '9':"wxyz"
12        }
13
14
15        res = []
16
17        def  rec(i, temp):
18            if i >= len(digits):
19                res.append("".join(temp[:]))
20                return
21            
22
23            al = digitsToChar[digits[i]]
24            for x in range(len(al)):
25                temp.append(al[x])
26                rec(i+1, temp)
27                temp.pop()
28        
29        rec(0, [])
30        return res